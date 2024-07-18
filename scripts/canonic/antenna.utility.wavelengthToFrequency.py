import sys
import argparse

from sys import stdin
from os import isatty
from scipy.constants import speed_of_light
from numpy import asarray

pars = argparse.ArgumentParser(prog="antenna.{'lnme': 'utility', 'desc': 'Utility functions'}.wavelengthToFrequency", description="wavelength to frequency conversion", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n\nformula:\n  f &= c0/\\lambda\n\n\n\nauthor(s):\n  Huseyin YIGIT, yigit.hsyn@gmail.com")
pars.add_argument("wavelength", help="wavelength in meters [m]", type=float, nargs="+")
pars.add_argument("--human", help="human readable output like kHz, MHz, GHz", action="store_true")
args = pars.parse_args(sys.argv[1:])

pipe = []
if not isatty(stdin.fileno()): 
  for line in stdin:
    pipe.append(line)
args.wlen = getattr(args, "wavelength") if getattr(args, "wavelength") else []
args.humn = getattr(args, "human") if getattr(args, "human") else False 

freq = speed_of_light / asarray(args.wlen, dtype="float") # type: ignore
for item in freq:
  if args.humn :
    if (item >= 1E12):
      print('%.1f THz'%(item / 1E12))
    elif (item >= 1E9):
      print('%.1f GHz'%(item / 1E9))
    elif (item >= 1E6):
      print('%.1f MHz'%(item / 1E6))
    elif (item >= 1E3):
      print('%.1f kHz' %(item/1E3))
  else:
    print('%.1f Hz' %(item))
