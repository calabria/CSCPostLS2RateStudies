'''
A simple script to easily submit all jobs for buffer rereco studies.
'''

import subprocess

version = 'v2'
datasets = ['HZZ', 'ZZ', 'Zprime']
failureStrings = ['0p00', '0p01', '0p02', '0p05', '0p10', '0p20', '0p03', '0p50', '1p00']
failureModes = ["BOTH", "CFEB", "DDU"]

for dataset in datasets:
    for failureString in failureStrings:
        for failureMode in failureModes:
            commandString = "farmoutAnalysisJobs $1 --merge --input-files-per-job=9999 --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/dntaylor/BufferOverload_%s_%s_%s_StandAlone_%s-makeStandAloneNtuple_cfg/ mergeBufferOverload_%s_%s_%s_%s $CMSSW_BASE" % (dataset, failureString, failureMode, version, dataset, failureString, failureMode, version)
            print commandString
            subprocess.call(commandString,shell=True)
