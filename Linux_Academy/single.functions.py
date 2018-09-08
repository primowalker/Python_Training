#!/usr/bin/python

import subprocess

def activeProcesses(lookup_user):
	processes_running = 0
	for line in subprocess.check_output("ps -ef", shell=True).splitlines()[1:]:
		user = line.split()[0]
		if lookup_user == user:
	    		processes_running+=1
	return "User %s has %s processes running" % (lookup_user, processes_running)

print activeProcesses('root')
print activeProcesses('f8tg2la')
