#!/usr/bin/python

''' get_swap_usage.py checks to see if the total amount 
	of swap used by the system is above a certain
	threshold.  If so, it will find the top 10 processes
	that are using the most swap and write those results
	to the log file /var/tmp/swap_usage.csv
'''

# Import modules
import commands
import sys
import time
import datetime

# Set the swap threshold
swap_usage_threshold = 80

# Check for swap usage
swap_cmd = commands.getoutput("free | grep Swap")
lines = swap_cmd.splitlines()
for line in lines:
        columns = line.split()

        # Get the total swap
        total_s = columns[1]

        # Get the used swap
        used_s = columns[2]

        # Convert to floating point
        total_swap = float(total_s)
        used_swap = float(used_s)

        # Get the percentage of used swap
        used_percentage = used_swap / total_swap

        # Convert it to an integer
        percentage = 100 * used_percentage
        percentage = int(percentage)

        ''' Compare the total used percentage to the threshold
			If equal to or above 80%, then get the top 10 processes
			using the most swap and write the results to the log file
		'''
		
		# Print a message saying that swap is above the threshold
        print "Swap usage log file written"
		
        if int(percentage) >= swap_usage_threshold:
                # Create the swap usage log file
                file = open('/var/tmp/swap_usage.csv', 'a')
                file.write("")
                file.close()

                # Get the top 10 processes using swap
                swap_processes_cmd = commands.getoutput("ps -eo vsz,user,pid,args | sort -nr | head -10")
                lines = swap_processes_cmd.splitlines()
                for line in lines:
                        columns = line.split()
                        # columns[0] = swap_used
                        # columns[1] = pid
                        # columns[2] = user
                        # columns[3] = process_name

                        # Get the current date the time
                        date_time = (time.strftime("%d-%m-%Y %H:%M:%S"))

                        # Write to the log file
                        file = open('/var/tmp/swap_usage.csv', 'a')
                        file.write(date_time + "," + columns[0] + "," + columns[1] + "," + columns[2] + "," + columns[3] + "\n")
                        file.close()
