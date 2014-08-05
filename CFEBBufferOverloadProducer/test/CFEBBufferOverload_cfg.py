import FWCore.ParameterSet.Config as cms

###
# Defaults
###
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')

options.inputFiles = "/store/user/dntaylor/GluGluToHToZZTo4m_M-125_14TeV-powheg-pythia6/GluGluToHToZZTo4m_M-125_14TeV-powheg-pythia6_GEM2019Upg14_RECO/140711_132140/0000/GEM2019Upg14_1.root"
options.outputFile = "GEM2019Upg14_Buffer.root"
options.register ('failureRate', 0.1, VarParsing.multiplicity.singleton, VarParsing.varType.float, "choose failure probability")
options.register ('latency', 20., VarParsing.multiplicity.singleton, VarParsing.varType.float, "choose L1A latency (microseconds)")
options.register ('l1aRate', 500., VarParsing.multiplicity.singleton, VarParsing.varType.float, "choose L1A rate (kHz)")
options.register ('doUniformFailure', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "run failure in all chambers evenly")
options.register ('doCFEBFailure', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "explicitly set CFEB failure")
options.register ('doDDUFailure', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "explicitly set DDU failure")
options.parseArguments()


process = cms.Process("ReRecoBuffer")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
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
    cscRecHitTag = cms.InputTag("csc2DRecHits"),
    failureRate = cms.untracked.double(options.failureRate),
    latency = cms.untracked.double(20.), # in microseconds
    l1aRate = cms.untracked.double(500.), # in kHz
    doUniformFailure = cms.untracked.bool(True),
    doCFEBFailure = cms.untracked.bool(True),
    doDDUFailure = cms.untracked.bool(True)
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
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')


# Path and EndPath definitions
process.cscLocalRecoOverload = cms.Sequence(process.csc2DRecHitsOverload*process.cscSegments)
process.preReco_step = cms.Path(process.cscLocalRecoOverload)
process.reconstruction_step = cms.Path(process.offlineBeamSpot * process.standAloneMuonSeeds * process.standAloneMuons * process.muonGlobalReco)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.out_step = cms.EndPath(process.out)

# Schedule definition
process.schedule = cms.Schedule(process.preReco_step,process.reconstruction_step,process.endjob_step,process.out_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2019WithGem

#call to customisation function cust_2019WithGem imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
process = cust_2019WithGem(process)

# End of customisation functions
