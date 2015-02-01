#!/usr/bin/python

from EEPROM_24C32 import EEPROM_24C32
import time
import datetime
import random

#=====================================================
# EEPROM_24C32_test : exercise EEPROM_24C32 class
#

ee_24c32 =  EEPROM_24C32(0x57, debug=False)

print 'EEPROM_24C32 test started'

print "----------------- "
print "----------------- "
print " Test the AT24C32 EEPROM"
print "----------------- "
print "writing first 10 addresses with random data"
for x in range(0,10):
	value = random.randint(0,255)
	print "address = %i writing value=%i" % (x, value) 	
	ee_24c32.write_AT24C32_byte(x, value)
print "----------------- "

print "reading first 10 addresses"
for x in range(0,10):
	print "address = %i value = %i" %(x, ee_24c32.read_AT24C32_byte(x)) 
print "----------------- "
print "----------------- "
