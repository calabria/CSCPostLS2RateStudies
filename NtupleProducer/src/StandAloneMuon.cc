#include "CSCPostLS2RateStudies/NtupleProducer/interface/StandAloneMuon.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include <DataFormats/TrackReco/interface/Track.h>
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/TrackReco/interface/HitPattern.h"

#include <cmath>
#include "TLorentzVector.h"

CSCDataFormats::StandAloneMuon::StandAloneMuon() 
{
}

CSCDataFormats::StandAloneMuon::~StandAloneMuon() 
{
}

void CSCDataFormats::StandAloneMuon::Set(const edm::Event& e, const edm::InputTag& muons_) 
{
   edm::Handle<std::vector<reco::Track>> muons;
   e.getByLabel(muons_,muons);

   sta_.muonSize = muons->size();

   int muonSize1p6 = 0;
   int muonSize2p1 = 0;

   for(std::vector<reco::Track>::const_iterator mu1=muons->begin(); mu1!=muons->end(); ++mu1){
      sta_.muStandAlonePt.push_back(mu1->pt());
      sta_.muStandAloneP.push_back(mu1->p());
      sta_.muStandAloneEta.push_back(mu1->eta());
      sta_.muStandAlonePhi.push_back(mu1->phi());

      if (abs(mu1->eta())>1.6) {
         muonSize1p6++;
         
         sta_.muStandAlonePt1p6.push_back(mu1->pt());
         sta_.muStandAloneP1p6.push_back(mu1->p());
         sta_.muStandAloneEta1p6.push_back(mu1->eta());
         sta_.muStandAlonePhi1p6.push_back(mu1->phi());
      }
      if (abs(mu1->eta())>2.1) {
         muonSize2p1++;
         
         sta_.muStandAlonePt2p1.push_back(mu1->pt());
         sta_.muStandAloneP2p1.push_back(mu1->p());
         sta_.muStandAloneEta2p1.push_back(mu1->eta());
         sta_.muStandAlonePhi2p1.push_back(mu1->phi());
      }
   }

   sta_.muonSize1p6 = muonSize1p6;
   sta_.muonSize2p1 = muonSize2p1;

   double ZMASS = 91.1876;
   double MUMASS = 0.105658;
   double Z1 = 0;
   TLorentzVector v1;
   TLorentzVector v2;
   TLorentzVector v;
   int numOSSF = numberOSSF(muons);
   if (numOSSF>0) {
      for(std::vector<reco::Track>::const_iterator mu1=muons->begin(); mu1!=muons->end(); ++mu1){
         for(std::vector<reco::Track>::const_iterator mu2=muons->begin(); mu2!=muons->end(); ++mu2){
            if (mu1==mu2) {
               continue;
            }
            if (mu1->charge()==mu2->charge()) {
               continue;
            }
            v1.SetPtEtaPhiM(mu1->pt(), mu1->eta(), mu1->phi(), MUMASS);
            v2.SetPtEtaPhiM(mu2->pt(), mu2->eta(), mu2->phi(), MUMASS);
            v = v1+v2;
            double Ztemp = v.M();
            if (abs(Ztemp-ZMASS)<abs(Z1-ZMASS)){
               Z1 = Ztemp;
            }
         }
      }
   }

   sta_.muStandAloneZ.push_back(Z1);
}

int CSCDataFormats::StandAloneMuon::numberOSSF(edm::Handle<std::vector<reco::Track>> muons)
{
   int numPlus = 0;
   int numMinus = 0;
   for(std::vector<reco::Track>::const_iterator mu1=muons->begin(); mu1!=muons->end(); ++mu1){
      if (mu1->charge()>0) {
         numPlus++;
      }
      else {
         numMinus++;
      }
   }
   return std::min(numPlus,numMinus);
}
