#!/usr/bin/python

from md03 import MD03
import time

#=====================================================
# MD03_test : exercise MD03 class
#

md03 =  MD03(0x58, debug=True)

print "MD03 test started"

md03.set_speed(50)
md03.set_accel(100)
md03.move_forward()
time.sleep(3)
md03.stop()
time.sleep(3)
print "Software revision = %d" % md03.read_reg(7)
