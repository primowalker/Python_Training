#!/usr/bin/python

import subprocess
lookup_user = 'root'
processes_running = 0
for line in subprocess.check_output("ps -ef", shell=True).splitlines()[1:]:
	user = line.split()[0]
	if lookup_user == user:
	    processes_running+=1
print "User %s has %s processes running" % (lookup_user, processes_running)
