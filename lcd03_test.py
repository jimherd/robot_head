#!/usr/bin/python

from lcd03 import LCD03
import time

#=====================================================
# LCD03_test : exercise LCD03 class
#

lcd03 = LCD03(0x63, debug=True)

print "LCD03 test started"

lcd03.clear()
lcd03.backlight_on()
lcd03.write_chr('J')
lcd03.write_str("im Herd")
sleep(5)
lcd03.backlight_off()
