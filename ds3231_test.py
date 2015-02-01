#!/usr/bin/python

from ds3231 import DS3231
import time
import datetime

#=====================================================
# DS3231_test : exercise D3231 class
#

ds3231 =  DS3231(0x68, debug=False)

print 'DS3231 test started'

ds3231.set_sqw(ds3231.FREQ4KHz, ds3231.EN_32KHz)

for i in range(0, 4):
  print 'seconds value = {0}'.format(ds3231.read_seconds())
  time.sleep(2.0)

#currenttime = datetime.datetime.utcnow()
#deltatime = currenttime - starttime
#print ""
#print "Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S")
print "DS3231= %s" % ds3231.read_datetime()
print "DS3231 Temp=", ds3231.getTemp()

