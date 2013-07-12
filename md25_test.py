#!/usr/bin/python

from md25 import MD25
import time

#=====================================================
# MD25_test : exercise MD25 class
#

md25 =  MD25(0x58, debug=True)

print 'MD03 test started'

md25.write_reg(15, 0)   # set mode 1
md25.write_reg(16, 0x20)    # reset encoders
md25.write_reg(16, 0x32)    # disable 2 second timeout

md25.write_reg(0, 200)     # turn on motor 1
md25.write_reg(1, 200)

for i in range(0, 9):
  print 'encoder 1 = {0}'.format(md25.read_encoder(1))
  print 'encoder 2 = {0}'.format(md25.read_encoder(2))
  time.sleep(2)
md25.write_reg(0, 128)
md25.write_reg(1, 128)

print 'Software revision = {0}'.format(md25.read_reg(13))
