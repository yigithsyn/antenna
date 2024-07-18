from sys import stdin
from os import isatty
from scipy.constants import speed_of_light
from numpy import asarray

snme = "wl2f"
lnme = "wavelengthToFrequency"
desc = "wavelength to frequency conversion"
auth = ["Huseyin YIGIT, yigit.hsyn@gmail.com"]
eplg = []
frml = ["f &= c0/\\lambda"]
refs = []

parg = [
  {"name": "wavelength", "desc": "wavelength in meters [m]", "type": "float", "cont": "+"}
]
oarg = []
flag = [
  {"name": "human", "desc": "human readable output like kHz, MHz, GHz"}
]

# testing
# from os import devnull
# from sys import stdout

class args:
  wlen = [1]
  humn = True
  debg = True

setattr(args, "wavelength", None)
setattr(args, "human", None)

if args.debg:
  freq = speed_of_light / args.wlen[0]
  assert freq == 299792458, "%s: Test failed."%lnme
  # stdout = open(devnull, "w")

# implementation
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
