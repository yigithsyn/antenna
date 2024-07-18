from sys import stdin, stdout
from os import isatty
from scipy.constants import speed_of_light
from numpy import asarray, power, set_printoptions, savetxt

snme = "gm2s"
lnme = "gammaToSwr"
desc = "reflection coefficient (gamma) to voltage standing wave ratio (vswr) conversion"
auth = ["Huseyin YIGIT, yigit.hsyn@gmail.com"]
eplg = []
frml = ["SWR &= \\dfrac{1+|\\Gamma|}{1-|\\Gamma|}"]
refs = []

parg = [
  {"name": "gamma", "desc": "reflection coefficient", "type": "float", "cont": "+"}
]
oarg = []
flag = [
  {"name": "db", "desc": "input reflection coefficient in dB"}
]

# testing
class args:
  gmma = [-10]
  dbsc = True
  debg = True

setattr(args, "gamma", None)
setattr(args, "db", None)

if args.debg:
  gmml = power(10,args.gmma[0]/20)
  vswr = (1+gmml)/(1-gmml)
  assert round(vswr,2) == 1.92, "%s: Test failed."%lnme

# implementation
pipe = []
if not isatty(stdin.fileno()): 
  for line in stdin:
    pipe.append(line)
args.gmma = pipe if pipe else getattr(args, "gamma") if getattr(args, "gamma") else []
args.dbsc = getattr(args, "db") if getattr(args, "db") else False

gmml = power(10,asarray(args.gmma,dtype="float")/20) if args.dbsc else asarray(args.gmma,dtype="float") 
savetxt(stdout,(1+gmml)/(1-gmml),fmt='%.3G')