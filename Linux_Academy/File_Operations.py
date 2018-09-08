#!/usr/bin/python

import os
import shutil

'''
	File creation, write, read
'''

# Open a new file for writing
file = open("/Users/jameswalker/iCloud/scripts/Linux_Academy/Test/test.txt", "w")
# Print the file information
print(file)

# Write something to the file
file.write("This is a test!")

# Close the file
file.close()
# Clear the file variable
file = None
# Open the file for reading
file = open("/Users/jameswalker/iCloud/scripts/Linux_Academy/Test/test.txt", "r")
# Read the file
file.read()

'''
	Check if a file or directory exists
'''
# Check to see if the file name exists
file = "/Users/jameswalker/iCloud/scripts/Linux_Academy/Test/test.txt"
if os.path.exists(file):
	print("Found it!")
else:
	print ("Nope, didn't fine it!")

# Check to see if the directory exists
dir = "/Users/jameswalker/iCloud/scripts/Linux_Academy/Test"
if os.path.isfile(dir):
	print ("It's a file!")

if os.path.isdir("/Users/jameswalker/iCloud/scripts/Linux_Academy/Test"):
	print("It's a directory!")

'''
	Copy, move, rename, delete files
'''

# Copy the text.txt file to the current working directory
shutil.copy("/Users/jameswalker/iCloud/scripts/Linux_Academy/Test/test.txt", "/Users/jameswalker/iCloud/scripts/Linux_Academy/test.txt")
# Check to see that the file is there
os.listdir()

# Rename test.txt
os.rename("/Users/jameswalker/iCloud/scripts/Linux_Academy/test.txt", "/Users/jameswalker/iCloud/scripts/Linux_Academy/test2.txt")
# Check to see that the file is there
os.listdir()

# Move test2.txt to the Test directory
shutil.move("/Users/jameswalker/iCloud/scripts/Linux_Academy/test2.txt", "/Users/jameswalker/iCloud/scripts/Linux_Academy/Test/test2.txt")
# Check to see that the file is there
os.listdir("/Users/jameswalker/iCloud/scripts/Linux_Academy/Test")

# Remove the test.txt and test2.txt files
os.remove("/Users/jameswalker/iCloud/scripts/Linux_Academy/Test/test.txt")
os.remove("/Users/jameswalker/iCloud/scripts/Linux_Academy/Test/test2.txt")
# Check to see that the files were removedirs
os.listdir("/Users/jameswalker/iCloud/scripts/Linux_Academy/Test")
# Remove the Test directory
os.removedirs("/Users/jameswalker/iCloud/scripts/Linux_Academy/Test")
# Check to see that the directory was removed
os.listdir("/Users/jameswalker/iCloud/scripts/Linux_Academy")




