#!/usr/bin/python

import re
line = "Nov 14 08:25:30 d1ppap1039 sshd[36460]: Accepted publickey for op01bmt from 10.180.5.237 port 37425 ssh2"
line2 = "Nov  4 00:02:40 shirazk2141 sshd[13506]: Invalid user jira from 87.249.204.63"
match = re.search('^(.*?)\s(\w+)\ssshd.*?Accepted\spublic.*?from\s(.*?)\sport.*?', line)
match2 = re.search('^(.*?)\s(\w+)\ssshd.*?Accepted\spublic.*?from\s(.*?)\sport.*?', line)
print match
print match2
print match.groups()
print match2.groups()

print match.group(1)
print match.group(2)
print match.group(3)

