#!/usr/bin/python

import commands # This imports the functions needed to get output from Linux OS commands

# Get the User CPU usage
cpu_usage_cmd1 = commands.getoutput("top -bn1 | head | grep Cpu | awk '{print $2}'")  # | sed 's/%//g' | sed 's/us,//g'")
# Get the System CPU usage
cpu_usage_cmd2 = commands.getoutput("top -bn1 | head | grep Cpu | awk '{print $3}'") # | sed 's/%//g' | sed 's/sy,//g'")

# Convert from string to floating point number
cpu1 = cpu_usage_cmd1.replace("%us,", "")
cpu2 = cpu_usage_cmd2.replace("%sy,", "")

# Get the sum of the two CPU usage values
total_cpu_usage = float(cpu1) + float(cpu2)

# Display the total CPU usage
print "Total CPU Usage is %s" % total_cpu_usage
