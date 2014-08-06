'''
A simple script to list the input files
'''

import subprocess
import os

version = 'v5'
datasets = ['HZZ', 'ZZ', 'Zprime']
failureStrings = ['0p00', '0p01', '0p02', '0p05', '0p10', '0p20', '0p03', '0p50', '1p00']
failureModes = ["BOTH", "CFEB", "DDU"]

subprocess.call("rm -rf inputs/inputs_BufferOverload*",shell=True)

for dataset in datasets:
    for failureString in failureStrings:
        for failureMode in failureModes:
            outstring = "inputs/inputs_BufferOverload_%s_%s_%s_%s.txt" % (dataset, failureString, failureMode, version)
            filestring = os.popen("ls /hdfs/store/user/dntaylor/BufferOverload_%s_%s_%s_%s-CFEBBufferOverload_cfg/*" % (dataset, failureString, failureMode, version)).read()
            print "saving to " + outstring
            file = open(outstring,"w")
            file.write(filestring.replace('/hdfs/','/'))
            file.close()
