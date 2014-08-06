# Auto generated configuration file
# using: 
# Revision: 1.20 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: GEM2019Upg14_ReReco --conditions auto:upgrade2019 --eventcontent=RECOSIM -s RECO --customise SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2019WithGem --geometry Extended2019 --magField 38T_PostLS1 --filein file:/hdfs/store/user/dntaylor/GluGluToHToZZTo4m_M-125_14TeV-powheg-pythia6/GluGluToHToZZTo4m_M-125_14TeV-powheg-pythia6_GEM2019Upg14_RECO/140711_132140/0000/GEM2019Upg14_1.root --fileout GEM2019Upg14_ReReco.root -n 100
import FWCore.ParameterSet.Config as cms

process = cms.Process('RERECO')

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

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:/hdfs/store/user/dntaylor/GluGluToHToZZTo4m_M-125_14TeV-powheg-pythia6/GluGluToHToZZTo4m_M-125_14TeV-powheg-pythia6_GEM2019Upg14_RECO/140711_132140/0000/GEM2019Upg14_1.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.20 $'),
    annotation = cms.untracked.string('GEM2019Upg14_ReReco nevts:100'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('GEM2019Upg14_ReReco.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')

# Path and EndPath definitions
process.reconstruction_step = cms.Path(process.reconstruction_fromRECO)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2019WithGem 

#call to customisation function cust_2019WithGem imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
process = cust_2019WithGem(process)

# End of customisation functions
