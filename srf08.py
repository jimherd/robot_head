#!/usr/bin/python

#========================================================
# SRF08 ultrasonic ranger driver
#
# Author : Jim Herd
# Date : May 2013
#
# Notes
#	Uses Adafruit_I2C module

from Adafruit_I2C import Adafruit_I2C

class SRF08 :
  i2c = None

# constructor
  def __init__(self, address=0x70, debug=False):
    self.i2c = Adafruit_I2C(address)
    self.address = address
    self.debug = debug

  def read_reg(self, reg): 
    if ((reg < 0 ) | (reg > 35)):
      if (self.debug):
	print "Register %d outwith range 0 to 35" % reg
	return -1 
    return self.i2c.readU8(reg)

  def write_reg(self, reg, val)
    if ((reg < 0) | (reg > 2):
      print "Register %d outwith range 0 to 2" % reg
      return -1
    self.i2c.write8(reg, val)
    return 0

  def read_echo(self, echo):
    if ((echo < 1) | (echo > 17)):
      if (self.debug):
        print "Echo request %d outwith range 1 to 17" % echo
    return self.i2c.readU16(((echo - 1) * 2) + 2))

