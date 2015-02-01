#!/usr/bin/env python
#
# Test SDL_DS3231
# John C. Shovic, SwitchDoc Labs
# 08/03/2014
#
#

# imports

import sys
from ds3231 import DS3231
import time
import datetime

# Main Program

print ""
print 'Setting time on DS3231'
print ""
print "Program Started at:" + time.strftime("%Y-%m-%d %H:%M:%S")
print ""

filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()

ds3231 =  DS3231(0x68, debug=False)
#comment out the next line after the clock has been initialized
ds3231.write_now()

#
#currenttime = datetime.datetime.utcnow()
#deltatime = currenttime - starttime
 
print ""
print "Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S")
	
print "DS3231=\t\t%s" % ds3231.read_datetime()

