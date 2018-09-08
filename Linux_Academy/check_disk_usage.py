#!/usr/bin/python

import subprocess

partition_usage_threshold = 55
df_cmd = subprocess.check_output(['df','-k'])

lines = df_cmd.splitlines()
for line in lines[1:]:
	columns = line.split()
	used_percentage = columns[4]
	used_percentage = used_percentage.replace('%','')
	if int(used_percentage) >= partition_usage_threshold:
		print "Partition %s is beyond the threshold at %s " % (columns[0], columns[4])
