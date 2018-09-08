#!/usr/bin/python
# Comprehension example

# Create a list of names starting with both upper and lower case letters.
names = ['jay', 'Lorraine', 'alex', 'olivia', 'nick', 'Nermal']
names_formated = [ x.title() for x in names]
print "These are the formated names: %s" % (names_formated)

# Format the names using  lambda math
names_formated = map(lambda x: x.title(), names)
print "These are the formated names using math lambda: %s" % (names_formated)

# Get names starting with N
names_starting_with_n = [name for name in names_formated if name[0].lower() == 'n' ]
print "These are the names starting with N: %s" % (names_starting_with_n)

