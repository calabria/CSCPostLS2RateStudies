from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'GEM2019Upg14_ZZ_RECO'
config.General.workArea = 'crab_GEM2019Upg14_ZZ'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'GEM2019Upg14_cfg.py'

config.section_("Data")
config.Data.inputDataset = '/ZZTo4mu_14TeV-powheg-pythia6/GEM2019Upg14-DES19_62_V8-v1/GEN-SIM'
config.Data.dbsUrl = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False

config.section_("Site")
config.Site.storageSite = 'T2_US_Wisconsin'

config.section_("User")
