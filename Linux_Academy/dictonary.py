#!/usr/bin/python

# Make a trafic dictornary
traffic_signal = {}
traffic_signal['red']='stop'
traffic_signal['yellow']='slow and stop'
traffic_signal['green']='go'
traffic_signal = { 'red' : 'stop', 'yellow' : 'slow and stop', 'green' : 'go'}

# Print the colors
print traffic_signal['green']
print traffic_signal['red']
print traffic_signal['yellow']

# Create a random coin toss dictonary
import random
results = {'heads' :0, 'tails' :0}
for i in range(0,1000):
	toss = random.randint(0,2)
	if toss == 1:
	    results['heads']+=1
	else:
	    results['tails']+=1

# Return on key at a time from dictonary result and return results one at a time.
for toss in results.keys():
	  print "Coinface %s showed up %s time" %(toss, results[toss])

	  