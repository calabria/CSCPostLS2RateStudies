# Auto generated configuration file
# using:
# Revision: 1.20
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step3 --filein file:HIG-TP2023HGCALDR-00029_step1.root --fileout file:HIG-TP2023HGCALDR-00029.root --pileup_input dbs:/MinBias_TuneZ2star_14TeV-pythia6/TP2023HGCALGS-DES23_62_V1-v3/GEN-SIM --mc --eventcontent RECOSIM --pileup AVE_140_BX_25ns --customise RecoParticleFlow/PandoraTranslator/customizeHGCalPandora_cff.cust_2023HGCalPandoraMuon,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RECO --conditions PH2_1K_FB_V6::All --step RAW2DIGI,L1Reco,RECO --magField 38T_PostLS1 --geometry Extended2023HGCalMuon,Extended2023HGCalMuonReco --python_filename step3_200MCHF_cfg.py --no_exec -n 1
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2023HGCalMuonReco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
                                       input = cms.untracked.int32(1)
                                       )

# Input source
process.source = cms.Source("PoolSource",
                            secondaryFileNames = cms.untracked.vstring(),
                            fileNames = cms.untracked.vstring('/store/mc/TP2023HGCALDR/GluGluToHToZZTo4m_M-125_14TeV-powheg-pythia6/GEN-SIM-DIGI-RAW/HGCAL_PU140BX25ForDT_newsplitPU140_PH2_1K_FB_V6-v1/50000/003B146F-9E0C-E511-9E69-0025905B85F6.root')
                            )

process.options = cms.untracked.PSet(

)

#--------------------------------------------------------------------------

# CSC
# case 0  :: all detectors in
# case 1  :: ME1/1 switched off
# case 2  :: ME2/1 switched off
# case 3  :: ME3/1 switched off
# case 4  :: ME4/1 switched off
# default :: all detectors in

# RPC
# case 0  :: NO RPC Upgrade
# case 1  :: RE3/1 switched off
# case 2  :: RE4/1 switched off
# case 3  :: RPC Upgrade switched on
# default :: all detectors in

#GEM
# case 0  :: all detectors off
# case 1  :: GE1/1 switched on
# case 2  :: GE2/1 switched on
# case 3  :: all detectors in
# default :: all detectors in

process.load('RecoLocalMuon.RPCRecHit.rpcRecHits_cfi')
process.load('RecoLocalMuon.GEMRecHit.gemRecHits_cfi')
process.load('RecoLocalMuon.CSCRecHitD.cscRecHitD_cfi')

#235 MCHF: GE2/1 + RE3/1 + RE4/1 switched off
process.csc2DRecHits.stationToUse = cms.untracked.int32(0)
process.rpcRecHits.recAlgoConfig.stationToUse = cms.untracked.int32(0)
process.gemRecHits.recAlgoConfig.stationToUse = cms.untracked.int32(0)

#--------------------------------------------------------------------------

# Production Info
process.configurationMetadata = cms.untracked.PSet(
                                                   version = cms.untracked.string('$Revision: 1.20 $'),
                                                   annotation = cms.untracked.string('step3 nevts:1'),
                                                   name = cms.untracked.string('Applications')
                                                   )

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
                                         splitLevel = cms.untracked.int32(0),
                                         eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                         outputCommands = process.RECOSIMEventContent.outputCommands,
                                         fileName = cms.untracked.string('file:step3.root'),
                                         dataset = cms.untracked.PSet(
                                                                      filterName = cms.untracked.string(''),
                                                                      dataTier = cms.untracked.string('GEN-SIM-RECO')
                                                                      )
                                         )

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(140.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/TP2023HGCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v3/00000/0010AE1F-6676-E411-8F16-002618943860.root', '/store/mc/TP2023HGCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v3/00000/0035CDEE-5C76-E411-8214-0023AEFDEEEC.root', '/store/mc/TP2023HGCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v3/00000/004B2C7D-6876-E411-ABFA-002618943949.root', '/store/mc/TP2023HGCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v3/00000/006DDC01-6276-E411-9E66-00259073E4E4.root', '/store/mc/TP2023HGCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v3/00000/008F6D89-5976-E411-A05E-549F35AC7DEE.root', '/store/mc/TP2023HGCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v3/00000/02133DBD-6176-E411-967A-002590A8882A.root', '/store/mc/TP2023HGCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v3/00000/0253431B-4F76-E411-ABFE-0025904C66F4.root', '/store/mc/TP2023HGCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v3/00000/02758CA9-5F76-E411-A1D8-0015172C07E1.root', '/store/mc/TP2023HGCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v3/00000/02C7F040-7176-E411-B19E-0023AEFDEE68.root', '/store/mc/TP2023HGCALGS/MinBias_TuneZ2star_14TeV-pythia6/GEN-SIM/DES23_62_V1-v3/00000/02DE880D-5576-E411-AE26-002590200A00.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'PH2_1K_FB_V6::All', '')

#--------------------------------------------------------------------------
# CSC aging

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    csc2DRecHitsOverload = cms.PSet(
        initialSeed = cms.untracked.uint32(81)
    ),
)

process.csc2DRecHitsOverload = cms.EDProducer('CFEBBufferOverloadProducer',
    cscRecHitTag = cms.InputTag("csc2DRecHits"),
    failureRate = cms.untracked.double(0.15),
    doUniformFailure = cms.untracked.bool(True),
    doCFEBFailure = cms.untracked.bool(True),
)

process.csclocalreco = cms.Sequence(process.csc2DRecHits*process.csc2DRecHitsOverload*process.cscSegments)

# change input to cscSegments
process.cscSegments.inputObjects = "csc2DRecHitsOverload"

#--------------------------------------------------------------------------

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)

#--------------------------------------------------------------------------
# DT aging

newlist28percent=[
    # MB4 of top sectors
    "WH-2_ST4_SEC2","WH-2_ST4_SEC3","WH-2_ST4_SEC4","WH-2_ST4_SEC5","WH-2_ST4_SEC6",
    "WH-1_ST4_SEC2","WH-1_ST4_SEC3","WH-1_ST4_SEC4","WH-1_ST4_SEC5","WH-1_ST4_SEC6",
    "WH0_ST4_SEC2","WH0_ST4_SEC3","WH0_ST4_SEC4","WH0_ST4_SEC5","WH0_ST4_SEC6",
    "WH1_ST4_SEC2","WH1_ST4_SEC3","WH1_ST4_SEC4","WH1_ST4_SEC5","WH1_ST4_SEC6",
    "WH2_ST4_SEC2","WH2_ST4_SEC3","WH2_ST4_SEC4","WH2_ST4_SEC5","WH2_ST4_SEC6",
    # MB1 of external wheels
    "WH-2_ST1_SEC1","WH-2_ST1_SEC2","WH-2_ST1_SEC3","WH-2_ST1_SEC4",
    "WH-2_ST1_SEC5","WH-2_ST1_SEC6","WH-2_ST1_SEC7","WH-2_ST1_SEC8",
    "WH-2_ST1_SEC9","WH-2_ST1_SEC10","WH-2_ST1_SEC11","WH-2_ST1_SEC12",
    "WH2_ST1_SEC1","WH2_ST1_SEC2","WH2_ST1_SEC3","WH2_ST1_SEC4",
    "WH2_ST1_SEC5","WH2_ST1_SEC6","WH2_ST1_SEC7","WH2_ST1_SEC8",
    "WH2_ST1_SEC9","WH2_ST1_SEC10","WH2_ST1_SEC11","WH2_ST1_SEC12",
    # 5 MB2s of external wheels
    "WH2_ST2_SEC3","WH2_ST2_SEC6","WH2_ST2_SEC9",
    "WH-2_ST2_SEC2","WH-2_ST2_SEC4",
    # more sparse failures
    "WH-2_ST2_SEC8","WH-1_ST1_SEC1","WH-1_ST2_SEC1","WH-1_ST1_SEC4","WH-1_ST3_SEC7",
    "WH0_ST2_SEC2","WH0_ST3_SEC5","WH0_ST4_SEC12","WH1_ST1_SEC6","WH1_ST1_SEC10","WH1_ST3_SEC3"
    ]

#from L1Trigger.L1IntegratedMuonTrigger.DTChamberMasker_cff import *
#appendChamberMaskerAtUnpacking(process,True,True,newlist28percent)

#--------------------------------------------------------------------------
# RPC aging

#from L1Trigger.L1IntegratedMuonTrigger.RPCChamberMasker_cff import *
#appendRPCChamberMaskerAtUnpacking(process,True,[637570221,637602989,637635757,637569201,637634737,637571545,637571677,637637213,637567793,637600561,637633329,637566989,637632525,637566993,637632529,637569037,637634573,637571565,637637101,637571449,637636985,637572317,637637853,637568057,637600825,637633593,637568025,637633561,637567381,637632917,637571805,637637341,637569325,637602093,637634861,637572569,637638105,637571569,637637105,637567065,637632601,637570229,637635765,637567285,637600053,637632821,637572589,637638125,637571157,637636693,637570485,637636021,637571181,637636717,637567069,637632605,637570365,637603133,637635901,637570481,637636017,637572445,637637981,637567005,637632541,637567373,637632909,637568509,637634045,637569425,637634961,637572561,637638097,637568409,637633945,637571281,637636817,637569973,637635509,637567157,637599925,637632693,637571197,637636733,637571321,637636857,637570237,637603005,637635773,637569453,637602221,637634989,637569977,637635513,637568305,637601073,637633841,637570097,637635633,637570197,637635733,637569709,637602477,637635245,637571161,637636697,637572429,637637965,637567669,637600437,637633205,637572045,637637581,637568301,637633837,637567213,637632749,637567801,637600569,637633337,637568053,637600821,637633589,637570109,637602877,637635645,637567965,637633501,637567993,637633529,637637081,637571193,637636729,637567281,637600049,637632817,637567469,637633005,637567953,637633489,637568177,637600945,637633713])

#reRunDttf( process )

#--------------------------------------------------------------------------

# customisation of the process.

# Automatic addition of the customisation function from RecoParticleFlow.PandoraTranslator.customizeHGCalPandora_cff
from RecoParticleFlow.PandoraTranslator.customizeHGCalPandora_cff import cust_2023HGCalPandoraMuon 

#call to customisation function cust_2023HGCalPandoraMuon imported from RecoParticleFlow.PandoraTranslator.customizeHGCalPandora_cff
process = cust_2023HGCalPandoraMuon(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
