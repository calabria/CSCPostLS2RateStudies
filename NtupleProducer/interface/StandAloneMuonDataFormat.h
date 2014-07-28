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
  };
}


#endif

