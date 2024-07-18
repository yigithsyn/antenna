import sys
import argparse

from sys import stdin, stdout
from os import isatty
from scipy.constants import speed_of_light
from numpy import asarray, power, set_printoptions, savetxt

pars = argparse.ArgumentParser(prog="antenna.{'lnme': 'utility', 'desc': 'Utility functions'}.gammaToSwr", description="reflection coefficient (gamma) to voltage standing wave ratio (vswr) conversion", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n\nformula:\n  SWR &= \\dfrac{1+|\\Gamma|}{1-|\\Gamma|}\n\n\n\nauthor(s):\n  Huseyin YIGIT, yigit.hsyn@gmail.com")
pars.add_argument("gamma", help="reflection coefficient", type=float, nargs="+")
pars.add_argument("--db", help="input reflection coefficient in dB", action="store_true")
args = pars.parse_args(sys.argv[1:])

pipe = []
if not isatty(stdin.fileno()): 
  for line in stdin:
    pipe.append(line)
args.gmma = pipe if pipe else getattr(args, "gamma") if getattr(args, "gamma") else []
args.dbsc = getattr(args, "db") if getattr(args, "db") else False

gmml = power(10,asarray(args.gmma,dtype="float")/20) if args.dbsc else asarray(args.gmma,dtype="float") 
savetxt(stdout,(1+gmml)/(1-gmml),fmt='%.3G')