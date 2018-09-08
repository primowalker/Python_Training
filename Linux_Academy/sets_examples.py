#!/usr/bin/python

# The sets_example.py gives several examples of how to use python sets

# Creat two sets of names
set1 = set(["James","Kyle","Brad","Sid","Nancy","Marvin","Zaphod"])
set2 = set(["James","Brad","Zaphod","Lewis","Mervin","Sherlock"])

print "These are the people in set 1: %s " % (set1)
print "These are the people in set 2: %s " % (set2)

# Find the common members of both sets
both_courses = set1 & set2
print "These people are in both sets: %s " % (both_courses)

# Find members who are in set2, but not set1
not_in_set1 = set2 - set1
print "These people are not in set 1: %s " % (not_in_set1)

# Find members who are in set1, but not in set2
not_in_set_2 = set1 - set2
print "These people are not in set 2: %s " % (not_in_set_2)