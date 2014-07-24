#ifndef __CSCDATAFORMATS_STANDALONEMUON_H__
#define __CSCDATAFORMATS_STANDALONEMUON_H__

#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"

#include "StandAloneMuonDataFormat.h"
#include <TMath.h>

namespace CSCDataFormats
{
  class StandAloneMuon
  {

  public:
    StandAloneMuon();
    ~StandAloneMuon();

    void Set(const edm::Event& e, const edm::InputTag& muons_);
    StandAloneMuonDataFormat* getData() {return &sta_;}
    void Reset() {sta_.Reset();}

  private:
    CSCDataFormats::StandAloneMuonDataFormat sta_;

  };
}


#endif
