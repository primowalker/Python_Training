#!//usr/bin/python

import random

test_score = random.randint(0,100)
if test_score >= 90:
	print "A"
elif test_score >= 80:
	print "B"
elif test_score >= 70:
	print "C"
elif test_score >= 60:
	print "D"
else:
	print "F"

print test_score
