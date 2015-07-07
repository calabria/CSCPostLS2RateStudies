import FWCore.ParameterSet.Config as cms

###
# Defaults
###
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')

options.inputFiles = "/store/relval/CMSSW_6_2_0_SLHC26_patch1/RelValMinBias_TuneZ2star_14TeV/GEN-SIM-RECO/DES19_62_V8_UP2019_des-v1/00000/FC4FDEE4-A41E-E511-A5EC-0025905A6090.root"
#options.inputFiles = "file:GEM2019Upg14.root"
options.outputFile = "GEM2019Upg14_Buffer.root"
options.register ('failureRate', 0.15, VarParsing.multiplicity.singleton, VarParsing.varType.float, "choose failure probability")
options.register ('doUniformFailure', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "run failure in all chambers evenly")
options.register ('doCFEBFailure', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "explicitly set CFEB failure")
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
#process.load('RecoMuon.Configuration.RecoMuon_cff')
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")


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
    doUniformFailure = cms.untracked.bool(True),
    doCFEBFailure = cms.untracked.bool(True),
)

# change input to cscSegments
process.cscSegments.inputObjects = "csc2DRecHitsOverload"

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(options.outputFile),
    outputCommands = cms.untracked.vstring('drop *',
      "keep *_standAloneMuons_*_ReRecoBuffer",
      "keep *_globalMuons_*_ReRecoBuffer",
      "keep *_muons_*_ReRecoBuffer",
      "keep *_csc2DRecHitsOverload_*_ReRecoBuffer",
      "keep *_csc2DRecHits_*_ReRecoBuffer",
      "keep *_cscSegments_*_ReRecoBuffer",
      "keep *_genParticles_*_*",
      "keep *_*uons_*_*",
    )
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')

process.TrackRefitter.TrajectoryInEvent = cms.bool(False)

# Path and EndPath definitions
process.cscLocalRecoOverload = cms.Sequence(process.csc2DRecHitsOverload*process.cscSegments)
process.preReco_step = cms.Path(process.cscLocalRecoOverload)
process.reconstruction_step = cms.Path(process.offlineBeamSpot * process.standAloneMuonSeeds * process.standAloneMuons)
process.localReReco = cms.Sequence()#process.siPixelRecHits+
                                   #process.siStripMatchedRecHits+
                                   #process.hbhereflag+
                                   #process.particleFlowCluster+
                                   #process.ecalClusters)
process.globalReReco =  cms.Sequence(process.offlineBeamSpot+
                                     #process.TrackRefitter+
                                     #process.recopixelvertexing+
                                     #process.ckftracks+
                                     #process.caloTowersRec+
                                     #process.vertexreco+
                                     #process.recoJets+
                                     process.muonrecoComplete)#+
                                     #process.muoncosmicreco+
                                     #process.egammaGlobalReco+
                                     #process.pfTrackingGlobalReco)#+
                                     #process.egammaHighLevelRecoPrePF+
                                     #process.muoncosmichighlevelreco+
                                     #process.metreco)
process.pfReReco = cms.Sequence()#process.particleFlowReco+
                                #process.egammaHighLevelRecoPostPF+
                                #process.muonshighlevelreco)#+
                                #process.particleFlowLinks+
                                #process.recoPFJets+
                                #process.recoPFMET+
                                #process.PFTau)
process.reconstruction_muons = cms.Path(
    process.offlineBeamSpot*
    process.standAloneMuonSeeds*
    process.standAloneMuons*
    process.refittedStandAloneMuons*
    process.globalmuontracking*
    process.muonIdProducerSequence*
    process.muIsolation*
    process.muonreco_with_SET*
    process.muonSelectionTypeSequence*
    process.pfReReco)
process.ReReco = cms.Path(process.standAloneMuonSeeds+process.localReReco+process.globalReReco+process.pfReReco)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.out_step = cms.EndPath(process.out)

# Schedule definition
process.schedule = cms.Schedule(process.preReco_step,process.ReReco,process.endjob_step,process.out_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
#from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2019WithGem
from SLHCUpgradeSimulations.Configuration.combinedCustoms import *

#call to customisation function cust_2019WithGem imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
#process = cust_2019WithGem(process)
process=customisePostLS1(process)
process=customisePhase1Tk(process)
process=customise_HcalPhase1(process)
process=jetCustoms.customise_jets(process)
process=customise_gem2019(process)

# End of customisation functions
