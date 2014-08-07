'''
A simple script to easily submit all jobs for buffer rereco studies.
'''

import subprocess

version = 'v8'
datasets = ['HZZ', 'ZZ', 'Zprime']
failureRates = [0., .01, .02, .05, .1, .2, .3, .5, 1.]
failureStrings = ['0p00', '0p01', '0p02', '0p05', '0p10', '0p20', '0p03', '0p50', '1p00']

for dataset in datasets:
    for failureRate,failureString in zip(failureRates,failureStrings):
        commandStringBoth = "farmoutAnalysisJobs $1 --input-file-list=inputs/inputs_GEM2019Upg14_%s.txt BufferOverload_%s_%s_BOTH_%s $CMSSW_BASE CSCPostLS2RateStudies/CFEBBufferOverloadProducer/test/CFEBBufferOverload_cfg.py 'outputFile=$outputFileName' 'inputFiles=$inputFileNames' 'failureRate=%f' 'doUniformFailure=True' 'doCFEBFailure=True' 'doDDUFailure=True'" % (dataset, dataset, failureString, version, failureRate)
        commandStringCFEBOnly = "farmoutAnalysisJobs $1 --input-file-list=inputs/inputs_GEM2019Upg14_%s.txt BufferOverload_%s_%s_CFEB_%s $CMSSW_BASE CSCPostLS2RateStudies/CFEBBufferOverloadProducer/test/CFEBBufferOverload_cfg.py 'outputFile=$outputFileName' 'inputFiles=$inputFileNames' 'failureRate=%f' 'doUniformFailure=True' 'doCFEBFailure=True' 'doDDUFailure=False'" % (dataset, dataset, failureString, version, failureRate)
        commandStringDDUOnly = "farmoutAnalysisJobs $1 --input-file-list=inputs/inputs_GEM2019Upg14_%s.txt BufferOverload_%s_%s_DDU_%s $CMSSW_BASE CSCPostLS2RateStudies/CFEBBufferOverloadProducer/test/CFEBBufferOverload_cfg.py 'outputFile=$outputFileName' 'inputFiles=$inputFileNames' 'failureRate=%f' 'doUniformFailure=True' 'doCFEBFailure=False' 'doDDUFailure=True'" % (dataset, dataset, failureString, version, failureRate)
        print commandStringBoth
        subprocess.call(commandStringBoth,shell=True)
        print commandStringCFEBOnly
        subprocess.call(commandStringCFEBOnly,shell=True)
        print commandStringDDUOnly
        subprocess.call(commandStringDDUOnly,shell=True)
