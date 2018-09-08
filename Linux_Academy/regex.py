#!/usr/bin/python

import re

# Set some text to parse
#line = "Nov 14 08:25:30 d1ppap1039 sshd[36460]: Accepted publickey for op01bmt from 10.180.5.237 port 37425 ssh2"
line = "Nov  4 00:02:40 shirazk2141 sshd[13506]: Invalid user jira from 87.249.204.63"

# Create unesscary and convolution regex code to match the line
#match = re.search('[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s\w*\ssshd\[\d*\]: Accepted publickey for \w* from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d* ssh2', line)
# Check for a match
#print match

# Create simpler regex code to get the date, server name, and IP
#match = re.search('^(.*?)\s(\w+)\ssshd.*?Accepted\spublic.*?from\s(.*?)\sport.*?', line)
match = re.search('^(.*?)\s(\w+)\ssshd.*?Invalid\suser.*?from\s(.*?)\sport.*?', line)

# The .* makes sure that it matches everything after it and the ?\s makes sure it stops when it comes to a space.
# Check for a match
#print match
# Print the match group
print match.group()
# Print each match group individually
print "Date: ", match.group(1)
print "Server: ", match.group(2)
print "IP: ", match.group(3)
