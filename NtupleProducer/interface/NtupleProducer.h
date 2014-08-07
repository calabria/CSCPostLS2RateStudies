#ifndef __CSCPOSTLS2RATESTUDIES_NTUPLEPRODUCER_H__
#define __CSCPOSTLS2RATESTUDIES_NTUPLEPRODUCER_H__

#include <memory>
#include <string>

#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "CSCPostLS2RateStudies/NtupleProducer/interface/StandAloneMuon.h"
#include "CSCPostLS2RateStudies/NtupleProducer/interface/StandAloneMuonDataFormat.h"

class TFile;
class TTree;


class NtupleProducer : public edm::EDAnalyzer {

  public:

   // constructor
      explicit NtupleProducer(const edm::ParameterSet&);
      virtual ~NtupleProducer();

   // fill tree
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void beginJob(void);
      virtual void endJob();

  private:

      edm::Service<TFileService> tfs_;
      TTree* tree_;

   // pat muons
      edm::InputTag muons_;
      edm::InputTag genParticles_;
      CSCDataFormats::StandAloneMuon* cscSTA;
      CSCDataFormats::StandAloneMuonDataFormat* cscSTA_data; 

};

#endif
