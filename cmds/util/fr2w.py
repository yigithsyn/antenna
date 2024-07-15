from scipy.constants import speed_of_light
from numpy import asarray

snme = "fr2w"
lnme = "frequencyToWavelength"
desc = "frequency to wavelength conversion"
eplg = []
frml = ["\\lambda &= c0/f"]
refs = []

parg = [
  {"name": "frequency", "desc": "frequency in Hertz [Hz]", "type": "float", "cont": "+"}
]
oarg = []
flag = [
  {"name": "human", "desc": "human readable output like cm, mm, km"}
]

# testing
# from os import devnull
# from sys import stdout

class args:
  freq = [1e6]
  humn = True
  debg = True

setattr(args, "frequency", None)
setattr(args, "human", None)

if args.debg:
  wlen = speed_of_light / args.freq[0]
  assert wlen == 299.792458, "%s: Test failed."%lnme
  # stdout = open(devnull, "w")

# implementation
args.freq = getattr(args, "frequency") if getattr(args, "frequency") else []
args.humn = getattr(args, "human") if getattr(args, "human") else False 

wlen = speed_of_light / asarray(args.freq)
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
