'''
A simple script to easily submit all jobs for buffer rereco studies.
'''

import subprocess

BufferVersion = 'v5'
version = 'v1'
datasets = ['HZZ', 'ZZ', 'Zprime']
failureStrings = ['0p00', '0p01', '0p02', '0p05', '0p10', '0p20', '0p03', '0p50', '1p00']
failureModes = ["BOTH", "CFEB", "DDU"]

for dataset in datasets:
    for failureString in failureStrings:
        for failureMode in failureModes:
            commandString = "farmoutAnalysisJobs $1 --input-file-list=inputs/inputs_BufferOverload_%s_%s_%s_%s.txt BufferOverload_%s_%s_%s_StandAlone_%s $CMSSW_BASE CSCPostLS2RateStudies/NtupleProducer/test/makeStandAloneNtuple_cfg.py 'outputFile=$outputFileName' 'inputFiles=$inputFileNames'" % (dataset, failureString, failureMode, BufferVersion, dataset, failureString, failureMode, version)
            print commandString
            subprocess.call(commandString,shell=True)
