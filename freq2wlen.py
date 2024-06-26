import sys
import argparse

import sys, os
from scipy import constants

parser = argparse.ArgumentParser(prog="freq2wlen", description="frequency to wavelength conversion", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="formula:\n\\lambda &= c0/f\n\n")
parser.add_argument("freq", help="frequency in Hertz [Hz]", type=float, nargs=1)
parser.add_argument("--human", help="human readable output like cm, mm, km", action="store_true")
args = parser.parse_args(sys.argv[1:])

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
