#!/usr/bin/python

import commands
partition_usage_threshold = 80

df_cmd = commands.getoutput("df -k")

lines = df_cmd.splitlines()
for line in lines[1:]:
	columns = line.split()
	used_percentage = columns[4]
	used_percentage = used_percentage.replace('%','')
	if int(used_percentage) >= partition_usage_threshold:
		print "partition %s usage is beyond threshold at %s " % (columns[0], columns[4])
	