#!//usr/bin/python

import platform
platform.linux_distribution()
('SUSE Linux Enterprise Server ', '11', 'x86_64')
sys_info = ' '.join(platform.linux_distribution())
sys_info
'SUSE Linux Enterprise Server  11 x86_64'
if "CentOS" in sys_info:
	print "CentOS"
elif "SUSE" in sys_info:
	print "SUSE OS"
elif "Red Hat" in sys_info:
	print "Red Hat OS"	
else:
	print "Unknown OS"

