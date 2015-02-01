#!/usr/bin/env python

# DS3231 object : based on SDL_DS3231.py Python Driver Code
# SwitchDoc Labs 12/19/2014

from Adafruit_I2C import Adafruit_I2C
from datetime import datetime

import time

class DS3231 :
  i2c = None

#constructor
  def __init__(self, address=0x68, debug=False):
    self.i2c = Adafruit_I2C(address)
    self.address       = address
    self.debug         = debug
    self._REG_SECONDS  = 0x00
    self._REG_MINUTES  = 0x01
    self._REG_HOURS    = 0x02
    self._REG_DAY      = 0x03
    self._REG_DATE     = 0x04
    self._REG_MONTH    = 0x05
    self._REG_YEAR     = 0x06
    self._REG_TEMP_MSB = 0x11
    self._REG_TEMP_LSB = 0x12
    self._REG_CONTROL  = 0x0E
    self._REG_CTRL_STAT= 0x0F

    self.FREQ1Hz   = 0
    self.FREQ1KHz  = 1
    self.FREQ4KHz  = 2
    self.FREQ8KHz  = 3
    self.FREQOFF   = 4

    self.DIS_32KHz = 0
    self.EN_32KHz  = 1

    self.i2c.write8(self._REG_CONTROL, 0b00011100)

# Decode a 2 BCD characters to a byte integer.
  def _bcd_to_int(self, bcd):
    out = (((bcd >> 4) & 0x0F) * 10) + (bcd & 0x0F)
    if (self.debug):
      print 'Seconds = {0}'.format(out)
    return out

# Encode a one or two digits number to the BCD.
  def _int_to_bcd(self, n):
    tens, units = divmod(n, 10)
    return (((tens << 4) & 0xF0) + units)

    ###########################
    # DS3231 Code
    ###########################

  def write_reg(self, reg, data):
    self.i2c.write8(reg, data)

  def read_reg(self, reg):
    return  self.i2c.readU8(reg)

  def read_seconds(self):
    return self._bcd_to_int(self.read_reg(self._REG_SECONDS) & 0x7F)

  def read_minutes(self):
    return self._bcd_to_int(self.read_reg(self._REG_MINUTES))

  def read_hours(self):
    d = self.read_reg(self._REG_HOURS)
    if ((d & 0b01000000) == 0b01000000):
      d = d & 0x1F      # 12 hour mode
    else:
      d = d & 0x3F      # 24 hour mode
    return self._bcd_to_int(d)

  def read_day(self):
    return self._bcd_to_int(self.read_reg(self._REG_DAY))

  def read_date(self):
    return self._bcd_to_int(self.read_reg(self._REG_DATE))

  def read_month(self):
    return self._bcd_to_int(self.read_reg(self._REG_MONTH))

  def read_year(self):
    return self._bcd_to_int(self.read_reg(self._REG_YEAR))

# Return a tuple such as (year, month, date, day, hours, minutes,seconds)
  def read_all(self):
    return (self.read_year(), self.read_month(), self.read_date(),
            self.read_day(), self.read_hours(), self.read_minutes(),
            self.read_seconds())

# Return a string such as 'YY-DD-MMTHH-MM-SS'.
  def read_str(self):
    return '%02d-%02d-%02dT%02d:%02d:%02d' % (self._read_year(),
         self.read_month(), self.read_date(), self.read_hours(),
         self.read_minutes(), self.read_seconds())

# Return the datetime.datetime object.  
  def read_datetime(self, century=21, tzinfo=None):
    return datetime((century - 1) * 100 + self.read_year(),
                self.read_month(), self.read_date(), self.read_hours(),
                self.read_minutes(), self.read_seconds(), 0, tzinfo=tzinfo)

# Direct write un-none value.
  def write_all(self, seconds=None, minutes=None, hours=None, day=None,
            date=None, month=None, year=None, save_as_24h=True):

#    Range: seconds [0,59], minutes [0,59], hours [0,23],
#           day [0,7], date [1-31], month [1-12], year [0-99].
    if seconds is not None:
      if seconds < 0 or seconds > 59:
        raise ValueError('Seconds is out of range [0,59].')
      seconds_reg = self._int_to_bcd(seconds)
      self.write_reg(self._REG_SECONDS, seconds_reg)
    if minutes is not None:
      if minutes < 0 or minutes > 59:
        raise ValueError('Minutes is out of range [0,59].')
      self.write_reg(self._REG_MINUTES, self._int_to_bcd(minutes))
    if hours is not None:
      if hours < 0 or hours > 23:
        raise ValueError('Hours is out of range [0,23].')
      self.write_reg(self._REG_HOURS, self._int_to_bcd(hours) ) # not  | 0x40 according to datasheet
    if year is not None:
      if year < 0 or year > 99:
        raise ValueError('Years is out of range [0,99].')
      self.write_reg(self._REG_YEAR, self._int_to_bcd(year))
    if month is not None:
      if month < 1 or month > 12:
        raise ValueError('Month is out of range [1,12].')
      self.write_reg(self._REG_MONTH, self._int_to_bcd(month))
    if date is not None:
      if date < 1 or date > 31:
        raise ValueError('Date is out of range [1,31].')
      self.write_reg(self._REG_DATE, self._int_to_bcd(date))
    if day is not None:
      if day < 1 or day > 7:
        raise ValueError('Day is out of range [1,7].')
      self.write_reg(self._REG_DAY, self._int_to_bcd(day))

# Write from a datetime.datetime object.
  def write_datetime(self, dt):
    self.write_all(dt.second, dt.minute, dt.hour,
                   dt.isoweekday(), dt.day, dt.month, dt.year % 100)

# Equal to DS3231.write_datetime(datetime.datetime.now()).
  def write_now(self):
    self.write_datetime(datetime.now())

# read temperature
  def getTemp(self):
#    return self.i2c.readS8(self._REG_TEMP_MSB)           # in units of 1 deg
    return  (self.i2c.readS16(self._REG_TEMP_MSB) / 64)   # in units of 0.25 deg

# set square wave output signals
  def set_sqw(self, extsqw, sq32K):

    ghost_control = self.i2c.readU8(self._REG_CONTROL) 
    print 'ghost_control = {0}'.format(ghost_control) 
    if (extsqw > self.FREQ8KHz):
      ghost_control = ghost_control | 0b00000100
    else: 
      ghost_control = ((ghost_control & 0b11100011) | (((extsqw << 3) & 0b00011000) & 0b11111011))
      print 'ghost_control = {0}'.format(ghost_control)
    self.i2c.write8(self._REG_CONTROL, ghost_control)

    ghost_ctrl_stat = self.i2c.readU8(self._REG_CTRL_STAT)
    if (sq32K == self.DIS_32KHz):
      ghost_ctrl_stat = ghost_ctrl_stat & 0b11110111   # clear bit
    elif (sq32K == self.EN_32KHz):
      ghost_ctrl_stat = ghost_ctrl_stat | 0b00001000   # set bit
    else:
      return # do nothing
    self.i2c.write8(self._REG_CTRL_STAT, ghost_ctrl_stat)

    


