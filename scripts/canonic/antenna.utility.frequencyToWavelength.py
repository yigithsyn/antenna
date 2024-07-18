import sys
import argparse

from sys import stdin
from os import isatty
from scipy.constants import speed_of_light
from numpy import asarray


pars = argparse.ArgumentParser(prog="antenna.{'lnme': 'utility', 'desc': 'Utility functions'}.frequencyToWavelength", description="frequency to wavelength conversion", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n\nformula:\n  \\lambda &= c0/f\n\n\n\nauthor(s):\n  Huseyin YIGIT, yigit.hsyn@gmail.com")
pars.add_argument("frequency", help="frequency in Hertz [Hz]", type=float, nargs="+")
pars.add_argument("--human", help="human readable output like cm, mm, km", action="store_true")
args = pars.parse_args(sys.argv[1:])

pipe = []
if not isatty(stdin.fileno()): 
  for line in stdin:
    pipe.append(line)
args.freq = pipe if pipe else getattr(args, "frequency") if getattr(args, "frequency") else []
args.humn = getattr(args, "human") if getattr(args, "human") else False

wlen = speed_of_light / asarray(args.freq, dtype="float") # type: ignore
for item in wlen:
  if args.humn :
    if item >= 1e3:
      print("%.1f km" % (item / 1e3))
    elif item >= 1:
      print("%.1f m" % (item / 1e0))
    elif item >= 1e-2:
      print("%.1f cm" % (item * 1e2))
    else:
      print("%.1f mm" % (item * 1e3))
  else:
    print("%.16G" % (item))
