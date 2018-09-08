#!/usr/bin/python

import time
import datetime

print "The current date and time is: ", (time.strftime("%d-%m-%Y %H:%M:%S"))
print "Time in seconds since the epoch: %s" % (time.time())
print "Current year: ", datetime.date.today().strftime("%Y")
print "Month of year: ", datetime.date.today().strftime("%B")
print "Week number of the year: ", datetime.date.today().strftime("%W")
print "Weekday of the week: ", datetime.date.today().strftime("%w")
print "Day of year: ", datetime.date.today().strftime("%j")
print "Day of the month : ", datetime.date.today().strftime("%d")
print "Day of week: ", datetime.date.today().strftime("%A")
print "Current month, day, year: ", datetime.date.today().strftime("%B_%d_%Y")
