#include "CSCPostLS2RateStudies/NtupleProducer/interface/NtupleProducer.h"

#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>

#include "TROOT.h"
#include "TTree.h"
#include "TFile.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Framework/interface/MakerMacros.h"

// Constructor
NtupleProducer::NtupleProducer(const edm::ParameterSet& ps) : tree_(0) {

   muons_ = ps.getParameter<edm::InputTag>("muons");

   cscSTA = new CSCDataFormats::StandAloneMuon();
   cscSTA_data = cscSTA->getData();

   tree_ = tfs_->make<TTree>("RecoTree", "RecoTree");
   tree_->Branch("StandAloneMuon", "CSCDataFormats::StandAloneMuonDataFormat", &cscSTA_data, 32000, 3);

}

NtupleProducer::~NtupleProducer() {
   
   delete cscSTA;

}

void NtupleProducer::beginJob(void) {
}

void NtupleProducer::endJob() {
}

void NtupleProducer::analyze(const edm::Event& e, const edm::EventSetup& es) {

   cscSTA->Reset();
   cscSTA->Set(e,muons_); 
   tree_->Fill();

}

DEFINE_FWK_MODULE( NtupleProducer );
