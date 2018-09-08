#!/usr/bin/python

import subprocess
users = {}

ps_cmd = subprocess.check_output(['ps','-ef'])

# Split the lines from ps -ef and exclude the first title line
for line in ps_cmd.splitlines()[1:]:
        # Get the user ID column from the ps -ef output
        user = line.split()[0]
        # Check to see if the user already exists in the dictonary. If not, add the user and increment.
        if users.get(user):
                users[user]+=1
        else:
                users[user]=1

# Remove non-root and low level system users from the users dict
del users['root'],users['daemon'],users['dbus'],users['rpc'],users['avahi']
print "Active non-root, low level system accounts on the system are " + ','.join(users.keys())

# Get the number of processes running per user. In this example, user.items counts the number of times a speficic user
# appears in the ps_cmd output.
for user, process_count in users.items():
        print "%s is running %s processes" % (user, process_count)

# Alternately, you can print the users with the number of times they appear like this:
print "This is another way to see the users and their number of processes"
print users
