import sys, os
from scipy import constants

name        = "freq2wlen"
description = "frequency to wavelength conversion"
epilogue    = ""
formula     = [
  "\\lambda &= c0/f"
]

positional_args = [
  {
    "name"        : "freq",       
    "description" : "frequency in Hertz [Hz]",
    "type"        : "float",
    "count"       : 1
  }
]

optional_args = []

flags = [
  {
    "name"        : "human",
    "description" : "human readable output like cm, mm, km"
  }
]

# testing
class args:
  freq  = [1E6]
  human = True
  debug = True
if args.debug:
  wavelength = constants.speed_of_light/args.freq[0]
  assert wavelength == 299.792458, "freq2wlen: Test failed."
  sys.stdout = open(os.devnull, 'w')


# implementation
wavelength = constants.speed_of_light/args.freq[0]
if args.human: 
  if (wavelength >= 1E3):
    print('%.1f km'%(wavelength / 1E3))
  elif (wavelength >= 1):
    print('%.1f m'%(wavelength / 1E0))
  elif (wavelength >= 1E-2):
    print('%.1f cm'%(wavelength * 1E2))
  else:
    print('%.1f mm' %(wavelength*1E3))
else:
  print('%.16G' %(wavelength))
