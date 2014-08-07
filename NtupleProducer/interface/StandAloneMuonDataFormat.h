#ifndef __CSCDATAFORMATS_STANDALONEMUONDATAFORMAT_H__
#define __CSCDATAFORMATS_STANDALONEMUONDATAFORMAT_H__

#include <TROOT.h>
#include <vector>
#include <iostream>

namespace CSCDataFormats
{
  struct StandAloneMuonDataFormat
  {
    StandAloneMuonDataFormat() {Reset();}
    ~StandAloneMuonDataFormat() {}
 
    void Reset()
    {
       muonSize = 0;
       muonSize1p6 = 0;
       muonSize2p1 = 0;

       muStandAlonePt.clear();
       muStandAloneP.clear();
       muStandAloneEta.clear();
       muStandAlonePhi.clear();

       muStandAlonePt1p6.clear();
       muStandAloneP1p6.clear();
       muStandAloneEta1p6.clear();
       muStandAlonePhi1p6.clear();

       muStandAlonePt2p1.clear();
       muStandAloneP2p1.clear();
       muStandAloneEta2p1.clear();
       muStandAlonePhi2p1.clear();

       muStandAloneZ.clear();
       muStandAloneZmumu.clear();

       muGenPt.clear();
       muGenP.clear();
       muGenEta.clear();
       muGenPhi.clear();

       muDeltaPt.clear();
       muResolution.clear();

       muGenPt1p6.clear();
       muGenP1p6.clear();
       muGenEta1p6.clear();
       muGenPhi1p6.clear();

       muDeltaPt1p6.clear();
       muResolution1p6.clear();

       muGenPt2p1.clear();
       muGenP2p1.clear();
       muGenEta2p1.clear();
       muGenPhi2p1.clear();

       muDeltaPt2p1.clear();
       muResolution2p1.clear();
    }

    int muonSize;
    int muonSize1p6;
    int muonSize2p1;
    
    // standalone muon properties
    std::vector<float> muStandAlonePt;
    std::vector<float> muStandAloneP;
    std::vector<float> muStandAloneEta;
    std::vector<float> muStandAlonePhi;

    std::vector<float> muStandAlonePt1p6;
    std::vector<float> muStandAloneP1p6;
    std::vector<float> muStandAloneEta1p6;
    std::vector<float> muStandAlonePhi1p6;

    std::vector<float> muStandAlonePt2p1;
    std::vector<float> muStandAloneP2p1;
    std::vector<float> muStandAloneEta2p1;
    std::vector<float> muStandAlonePhi2p1;

    std::vector<float> muStandAloneZ;
    std::vector<float> muStandAloneZmumu;

    std::vector<float> muGenPt;
    std::vector<float> muGenP;
    std::vector<float> muGenEta;
    std::vector<float> muGenPhi;

    std::vector<float> muDeltaPt;
    std::vector<float> muResolution;

    std::vector<float> muGenPt1p6;
    std::vector<float> muGenP1p6;
    std::vector<float> muGenEta1p6;
    std::vector<float> muGenPhi1p6;

    std::vector<float> muDeltaPt1p6;
    std::vector<float> muResolution1p6;

    std::vector<float> muGenPt2p1;
    std::vector<float> muGenP2p1;
    std::vector<float> muGenEta2p1;
    std::vector<float> muGenPhi2p1;

    std::vector<float> muDeltaPt2p1;
    std::vector<float> muResolution2p1;

  };
}


#endif

