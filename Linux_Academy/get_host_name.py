#!/usr/bin/python

import subprocess

host_name = subprocess.check_output("hostname")
print host_name
