#!/usr/bin/python
# Basic_File_Operations-2.py

import os

# Get the current working directory
os.getcwd()

# Get a list of directory paths, names, and file names
for dirpath, dirnames, filenames in os.walk(os.getcwd(), topdown="true"):
	print(dirpath, filenames)

# Get a list of directory paths and file names, but make the output nice
for dirpath, dirnames, filenames in os.walk(os.getcwd(), topdown="true"):
	for filename in filenames:
		print(dirpath, filename)
