'''
A simple script to easily submit all jobs for buffer rereco studies.
'''

import subprocess

version = 'v1'
datasets = ['HZZ', 'ZZ', 'Zprime']
failureStrings = ['0p00', '0p01', '0p02', '0p05', '0p10', '0p20', '0p03', '0p50', '1p00']
failureModes = ["BOTH", "CFEB", "DDU"]

for dataset in datasets:
    for failureString in failureStrings:
        for failureMode in failureModes:
            commandString = "cp /hdfs/store/user/dntaylor/mergeBufferOverload_%s_%s_%s_%s-mergeFilesJob/*.root rootFiles/BufferOverload_%s_%s_%s.root" % (dataset, failureString, failureMode, version, dataset, failureString, failureMode)
            print commandString
            subprocess.call(commandString,shell=True)
