#!/usr/bin/env python

# Based on SDL_DS3231.py Python Driver Code
# SwitchDoc Labs 12/19/2014

from Adafruit_I2C import Adafruit_I2C

import time
import smbus

class EEPROM_24C32():
  i2c = None

  def __init__(self, address=0x57, debug=False ):
        self.i2c = Adafruit_I2C(address)
        self.address = address
        self.debug = debug

    ###########################
    # AT24C32 Code
    ###########################

  def set_current_AT24C32_address(self, address):
    a1=address / 256;
    a0=address % 256;
    self.i2c.writeList(a1, [a0])
#    self._bus.write_i2c_block_data(self.address, a1, [a0])

  def read_AT24C32_byte(self, address):
    self.set_current_AT24C32_address(address)
    return self.i2c.readU8_noreg()
#    return smbus.bus.read_byte(self.address)

  def write_AT24C32_byte(self, address, value):
    #print "i2c_address =0x%x eepromaddress = 0x%x value = 0x%x %i " % (self._at24c32_addr, address, value, value)
	
    a1=address / 256;
    a0=address % 256;
    self.i2c.writeList(a1, [a0, value])
#    self._bus.write_i2c_block_data(self._at24c32_addr,a1,[a0, value])
    time.sleep(0.20)



