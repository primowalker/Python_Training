#!/usr/bin/python

import subprocess
def activeProcesses(lookup_user, lookup_cmd):
        processes_running_all = 0
        processes_running_searched = 0
        for line in subprocess.check_output("ps -ef", shell=True).splitlines()[1:]:
                user = line.split()[0]
                if lookup_user == user:
                        processes_running_all+=1
                        if lookup_cmd in line:
                                processes_running_searched+=1
        return processes_running_all, processes_running_searched

procs_total, procs_searched = activeProcesses('root', 'xfs')
print "Total root processes running %s " % (procs_total)
print "Total xfs processes running %s  " % (procs_searched)
