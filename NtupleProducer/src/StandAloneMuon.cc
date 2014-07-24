#include "CSCPostLS2RateStudies/NtupleProducer/interface/StandAloneMuon.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include <DataFormats/TrackReco/interface/Track.h>
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/TrackReco/interface/HitPattern.h"

#include <cmath>

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
      sta_.muStandAloneEta.push_back(mu1->eta());
      sta_.muStandAlonePhi.push_back(mu1->phi());

      if (abs(mu1->eta())>1.6) {
         muonSize1p6++;
         
         sta_.muStandAlonePt1p6.push_back(mu1->pt());
         sta_.muStandAloneEta1p6.push_back(mu1->eta());
         sta_.muStandAlonePhi1p6.push_back(mu1->phi());
      }
      if (abs(mu1->eta())>2.1) {
         muonSize2p1++;
         
         sta_.muStandAlonePt2p1.push_back(mu1->pt());
         sta_.muStandAloneEta2p1.push_back(mu1->eta());
         sta_.muStandAlonePhi2p1.push_back(mu1->phi());
      }
   }

   sta_.muonSize1p6 = muonSize1p6;
   sta_.muonSize2p1 = muonSize2p1;
}
