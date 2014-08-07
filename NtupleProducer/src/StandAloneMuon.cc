#include "CSCPostLS2RateStudies/NtupleProducer/interface/StandAloneMuon.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include <DataFormats/TrackReco/interface/Track.h>
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/TrackReco/interface/HitPattern.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"

#include <cmath>
#include "TLorentzVector.h"

CSCDataFormats::StandAloneMuon::StandAloneMuon() 
{
}

CSCDataFormats::StandAloneMuon::~StandAloneMuon() 
{
}

void CSCDataFormats::StandAloneMuon::Set(const edm::Event& e, const edm::InputTag& muons_, const edm::InputTag& genParticles_) 
{
   edm::Handle<std::vector<reco::Track>> muons;
   e.getByLabel(muons_,muons);

   edm::Handle<std::vector<reco::GenParticle>> genParticles;
   e.getByLabel(genParticles_,genParticles);

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

      for(std::vector<reco::GenParticle>::const_iterator gen1=genParticles->begin(); gen1!=genParticles->end(); ++gen1){
         if (std::abs(gen1->pdgId())==13) {
            // Match to muon by deltaR (take first match)
            if (std::abs(deltaR<reco::Track,reco::GenParticle>(*mu1,*gen1))<0.1) {
               sta_.muGenPt.push_back(gen1->pt());
               sta_.muGenP.push_back(gen1->p());
               sta_.muGenEta.push_back(gen1->eta());
               sta_.muGenPhi.push_back(gen1->phi());

               sta_.muDeltaPt.push_back(mu1->pt()-gen1->pt());
               sta_.muResolution.push_back((mu1->pt()-gen1->pt())/gen1->pt());

               if (abs(mu1->eta())>1.6) {
                  sta_.muGenPt1p6.push_back(gen1->pt());
                  sta_.muGenP1p6.push_back(gen1->p());
                  sta_.muGenEta1p6.push_back(gen1->eta());
                  sta_.muGenPhi1p6.push_back(gen1->phi());

                  sta_.muDeltaPt1p6.push_back(mu1->pt()-gen1->pt());
                  sta_.muResolution1p6.push_back((mu1->pt()-gen1->pt())/gen1->pt());
               }

               if (abs(mu1->eta())>2.1) {
                  sta_.muGenPt2p1.push_back(gen1->pt());
                  sta_.muGenP2p1.push_back(gen1->p());
                  sta_.muGenEta2p1.push_back(gen1->eta());
                  sta_.muGenPhi2p1.push_back(gen1->phi());

                  sta_.muDeltaPt2p1.push_back(mu1->pt()-gen1->pt());
                  sta_.muResolution2p1.push_back((mu1->pt()-gen1->pt())/gen1->pt());
               }
               break; // found matching
            }
         }
      }
   }

   sta_.muonSize1p6 = muonSize1p6;
   sta_.muonSize2p1 = muonSize2p1;

   double ZMASS = 91.1876;
   double MUMASS = 0.105658;
   double Z1 = -99999;
   double Zmumu = -99999;
   double pt1 = -99999;
   double pt2 = -99999;
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
            if (mu1->pt()>=pt1) {
               if (mu2->pt()>=pt2) {
                  Zmumu = Ztemp;
               }
            }
         }
      }
   }

   sta_.muStandAloneZ.push_back(Z1);
   sta_.muStandAloneZmumu.push_back(Zmumu);
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
