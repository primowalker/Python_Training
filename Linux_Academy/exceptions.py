#!/usr/bin/python

try:
	print 1/0
except ZeroDivisionError:
	print "Cannot divide by a zero"
else:
	print "All good"


try:
	import subprocess
	subprocess.check_output(['k'])
		except Exception as ex:
	print "A %s exception happened because %s" % (type(ex).__name__, ex.args)
		else:
	print "all good"
