// -*- C++ -*-
//
// Package:    CFEBBufferOverloadProducer
// Class:      CFEBBufferOverloadProducer
// 
/**\class CFEBBufferOverloadProducer CFEBBufferOverloadProducer.cc CSCPostLS2RateStudies/CFEBBufferOverloadProducer/plugins/CFEBBufferOverloadProducer.cc

 Description: A producer to randomly remove CFEB digis in the inner muon rings.

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Devin Taylor
//         Created:  Sun, 13 Jul 2014 10:55:48 GMT
// $Id$
//
//


// system include files
#include <memory>
#include <boost/random/random_device.hpp>
#include <boost/random.hpp>
#include <math.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include <DataFormats/Common/interface/Handle.h>
#include <FWCore/Framework/interface/ESHandle.h>

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "CLHEP/Random/RandomEngine.h"

#include <Geometry/Records/interface/MuonGeometryRecord.h>

#include <DataFormats/CSCRecHit/interface/CSCRecHit2DCollection.h>
#include <DataFormats/MuonDetId/interface/CSCDetId.h>

//
// class declaration
//

class CSCGeometry;
class CSCDetId;

class CFEBBufferOverloadProducer : public edm::EDProducer {
   public:
      explicit CFEBBufferOverloadProducer(const edm::ParameterSet&);
      ~CFEBBufferOverloadProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      
      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      bool checkOverload(int station, CLHEP::HepRandomEngine& engine);

      // ----------member data ---------------------------
      edm::EDGetTokenT<CSCRecHit2DCollection> rh_token;
      double failureRate_;

      const CSCGeometry* geom_;
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
CFEBBufferOverloadProducer::CFEBBufferOverloadProducer(const edm::ParameterSet& iConfig)
{
   failureRate_ = iConfig.getUntrackedParameter<double>("failureRate",0.1);
   // consumes
   rh_token = consumes<CSCRecHit2DCollection>( iConfig.getParameter<edm::InputTag>("cscRecHitTag") );

   //register your products
   produces<CSCRecHit2DCollection>();

}


CFEBBufferOverloadProducer::~CFEBBufferOverloadProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
CFEBBufferOverloadProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   // Get the CSC Geometry :
   edm::ESHandle<CSCGeometry> cscGeom;
   iSetup.get<MuonGeometryRecord>().get(cscGeom);

   // get random number generator
   edm::Service<edm::RandomNumberGenerator> rng;
   CLHEP::HepRandomEngine& engine = rng->getEngine();

   // Get the RecHits collection :
   edm::Handle<CSCRecHit2DCollection> recHits;
   iEvent.getByToken( rh_token, recHits );

   // Create empty collection of rechits  
   std::auto_ptr<CSCRecHit2DCollection> oc( new CSCRecHit2DCollection );

   // Vector to store rechit within layer
   std::vector<CSCRecHit2D> hitsInLayer;
 
   //std::cout << "Selecting Overloaded Buffers" << std::endl;
   bool bufferOverloaded[2][4][4][36][7] = {{{{{0}}}}}; //endcap, station, ring, chamber, cfeb
   // iterate over each cfeb and decide if it had a buffer overload
   for (int endcap=1; endcap<3; endcap++) {
      for (int station=2; station<5; station++) {
         for (int chamber=1; chamber<19; chamber++) {
            for (int cfeb=1; cfeb<6; cfeb++) { 
               bufferOverloaded[endcap-1][station-1][0][chamber-1][cfeb-1] = checkOverload(station,engine);
               //if (bufferOverloaded[endcap-1][station-1][0][chamber-1][cfeb-1]) {
               //   std::cout << "  E: " << std::to_string(endcap) 
               //             << " S: " << std::to_string(station) 
               //             << " R: 1 C: " << std::to_string(chamber) 
               //             << " B: " << std::to_string(cfeb) << std::endl;
               //}
            }
         }
      }
   }

   //iterate over each rechit, get detector id, check if in overloaded cfeb, store in new collection
   CSCDetId prevId;
   CSCDetId currId;
   //std::cout << "Iterating over CSCRecHit2D" << std::endl;
   for (CSCRecHit2DCollection::const_iterator it=recHits->begin(); it!=recHits->end(); it++) {
      CSCRecHit2D hit = (*it);
      currId = (CSCDetId)hit.cscDetId();
      if (currId!=prevId) { //if we are moving on to the next detector
         if (!hitsInLayer.empty()) {
            //std::cout << "   " << prevId << " (" << std::to_string(hitsInLayer.size()) << " CSCRecHits added)" << std::endl;
            oc->put(prevId, hitsInLayer.begin(), hitsInLayer.end());
            hitsInLayer.clear();
         }
         hitsInLayer.clear();
      }
      prevId = currId;
      int numStrips = hit.nStrips();
      int strip = ((numStrips==3) ? hit.channels(1) : hit.channels(0));
      int cfeb = ceil(strip/80.0);
      //std::cout << "CSCDetID: " << currId << " B: " << std::to_string(cfeb);
      if (!bufferOverloaded[currId.endcap()-1][currId.station()-1][currId.ring()-1][currId.chamber()-1][cfeb-1]) {
         //std::cout << " added" << std::endl;
         hitsInLayer.push_back(hit);
      }
      //else {
      //   std::cout << " not added" << std::endl;
      //}
   }

   //std::cout << "Done processing overloaded buffers" << std::endl;
   iEvent.put(oc);
}

bool
CFEBBufferOverloadProducer::checkOverload(int station, CLHEP::HepRandomEngine& engine)
{
   double randomNumber = engine.flat();
   return (randomNumber<failureRate_);
}

// ------------ method called once each job just before starting event loop  ------------
void 
CFEBBufferOverloadProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CFEBBufferOverloadProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
/*
void
CFEBBufferOverloadProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
CFEBBufferOverloadProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
CFEBBufferOverloadProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
CFEBBufferOverloadProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CFEBBufferOverloadProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(CFEBBufferOverloadProducer);
