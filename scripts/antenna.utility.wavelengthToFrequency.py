import sys, os, argparse
import scipy
import numpy

snme = "ante.util.wl2f"                                   # short name
lnme = "antenna.utility.wavelengthToFrequency"            # long name
desc = "wavelength to frequency conversion"               # description
fncs = []                                                 # functions
expl = []                                                 # explanation
frml = [                                                  # formulas 
  "f &= c0/\\lambda"
]
auth = [                                                  # authors
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = []                                                 # references
parg = [                                                  # positional arguments
  {"name": "wavelength", "desc": "wavelength in meters [m]", "type": float, "cont": "+"}
]
oarg = []                                                 # optional arguments
flag = [                                                  # flags
  {"name": "human", "desc": "human readable output like kHz, MHz, GHz"}
]

# preparation for parsing 
flst = []                                                 # function list
for i in range(len(fncs)):
  flst.append("  %s: %s"%(fncs[i]["snme"].ljust(4),fncs[i]["desc"]))
for i in range(len(frml)):
  frml[i] = "  " + frml[i]
for i in range(len(expl)):
  expl[i] = "  " + expl[i]
for i in range(len(auth)):
  auth[i] = "  " + auth[i]
for i in range(len(refs)):
  refs[i] = "  - " + refs[i]

# argument parsing 
class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help(sys.stderr)
        exit(2)
pars = ArgumentParser(prog=lnme,  
                      description="%s%s%s"%(
                        desc,
                        '\n\nfunctions:\n' if fncs else '','\n'.join(flst)),
                      formatter_class=argparse.RawDescriptionHelpFormatter, 
                      epilog="%s%s%s%s%s%s%s%s"%(
                        '\n\nexplanation:\n' if expl else '','\n'.join(expl),
                        '\n\nformula:\n' if frml else '','\n'.join(frml),
                        '\n\nauthor:\n' if auth else '','\n'.join(auth),
                        '\n\nreferences:\n' if refs else '','\n'.join(refs)))
for item in parg:
  pars.add_argument(item["name"], help=item["desc"], type=item["type"], nargs=item["cont"])
for item in oarg:
  pars.add_argument("--"+item["name"], help=item["desc"], type=item["type"], default=item["default"], nargs=item["cont"])
for item in flag:
  pars.add_argument("--"+item['name'], help=item['desc'], action="store_true")
if not os.isatty(sys.stdin.fileno()): 
  for line in reversed(list(sys.stdin)):
    sys.argv = sys.argv[:1] + [line.rstrip()] + sys.argv[1:]
args = pars.parse_args(sys.argv[1:])

# implementation
freq = scipy.constants.speed_of_light / numpy.asarray(getattr(args,"wavelength"), dtype="float")
if getattr(args,"human"):
  for item in freq:
    if (item >= 1E12):
      print('%.1f THz'%(item / 1E12))
    elif (item >= 1E9):
      print('%.1f GHz'%(item / 1E9))
    elif (item >= 1E6):
      print('%.1f MHz'%(item / 1E6))
    elif (item >= 1E3):
      print('%.1f kHz' %(item/1E3))
else:
  numpy.savetxt(sys.stdout,freq,fmt='%.1G')
