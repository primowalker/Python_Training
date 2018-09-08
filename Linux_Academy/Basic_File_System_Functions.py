#!/usr/bin/python
# Basic_File_Operations-1.py

import os

# Get the current working directory
os.getcwd()

# List the contents of the current directory
os.listdir()

# List the contents of /var/log
ls.listdir("/var/log")

# Make a directory called Test in the current directory
os.mkdir("Test")

# Change to the Test dirctory
os.chdir("Test")

# Change back to the home dirctory
os.chdir("/Users/jameswalker")

# Get a list of directory paths, names, and file names
for dirpath, dirnames, filenames in os.walk(os.getcwd(), topdown="true"):
    
