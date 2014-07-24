import FWCore.ParameterSet.Config as cms

###
# Defaults
###
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')

options.inputFiles = "/store/mc/Summer12/GluGluToHToZZTo4L_M-125_14TeV-powheg-pythia6/GEN-SIM-RAW-RECO/PU50bx25_POSTLS161_V12-v1/10000/0004A91B-754C-E211-9FEA-00304867BEDE.root"
options.outputFile = "POSTLS1_PU50bx25_Buffer.root"
options.parseArguments()


process = cms.Process("ReRecoBuffer")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryIdeal_cff.py')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        options.inputFiles
    )
)

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    csc2DRecHitsOverload = cms.PSet(
        initialSeed = cms.untracked.uint32(81)
    ),
)

process.csc2DRecHitsOverload = cms.EDProducer('CFEBBufferOverloadProducer',
    cscRecHitTag = cms.InputTag("csc2DRecHits")

)

# change input to cscSegments
process.cscSegments.inputObjects = "csc2DRecHitsOverload"

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(options.outputFile),
    outputCommands = cms.untracked.vstring('drop *',
      "keep *_standAloneMuons_*_ReRecoBuffer",
      "keep *_globalMuons_*_ReRecoBuffer",
      "keep *_csc2DRecHitsOverload_*_ReRecoBuffer",
      "keep *_csc2DRecHits_*_ReRecoBuffer",
      "keep *_cscSegments_*_ReRecoBuffer",
    )

)

process.options = cms.untracked.PSet(

)

# Additional output definition

# Other statements
process.GlobalTag = 'POSTLS162_V6::All'


# Path and EndPath definitions
process.cscLocalRecoOverload = cms.Sequence(process.csc2DRecHitsOverload*process.cscSegments)
process.preReco_step = cms.Path(process.cscLocalRecoOverload)
process.reconstruction_step = cms.Path(process.offlineBeamSpot * process.standAloneMuonSeeds * process.standAloneMuons * process.muonGlobalReco)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.out_step = cms.EndPath(process.out)

# Schedule definition
process.schedule = cms.Schedule(process.preReco_step,process.reconstruction_step,process.endjob_step,process.out_step)

