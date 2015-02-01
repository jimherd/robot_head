#!/usr/bin/python

import sys
from srf08 import SRF08

#=====================================================
# SRF08_test : exercise SRF08 class
#

print 'SRF08 address change program'

if (len(sys.argv) != 3):
  print 'Usage : srf08_change_address  old_address   new_address'
  sys.exit(0)

srf08 =  SRF08(int(sys.argv[1], 16), debug=True)
srf08.change_address(int(sys.argv[1], 16), int(sys.argv[2], 16))

print 'SRF08 address change complete'
