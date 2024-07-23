import sys, os, argparse
import scipy
import numpy

snme = "ante.meas.mnfr"                                   # short name
lnme = "antenna.measurement.miniumumNearFieldDistance"    # long name
desc = "minimum recommended distance for near-field antenna measurements in meters" # description             
fncs = []                                                 # functions
expl = [                                                  # explanation
  "Standard suggests to choose between 3 or 5 wavelength.",
  "In order to ensure copuling effect, 5 wavelength distance is choosen and implemented."
]
frml = [                                                  # formulas 
 "R_{nf} &= 5\\times\\lambda = 5\\times c_0/f"
]
auth = [                                                  # authors
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = [                                                  # references
  "[IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.3.1.4, Page 27](https://ieeexplore.ieee.org/document/6375745)",
]
parg = [                                                  # positional arguments
  {"name": "frequency", "desc": "frequency of interest in Hertz [Hz]", "type": float, "cont": "+"}
]
oarg = []                                                 # optional arguments
flag = [                                                  # flags
  {"name": "human", "desc": "human readable output like mm, cm, m"}
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
nfr = 5*scipy.constants.speed_of_light / numpy.asarray(getattr(args,"frequency"), dtype="float")
if getattr(args,"human"):
  for item in nfr:
    if item >= 1e3:
      print("%.1f km" % (item / 1e3))
    elif item >= 1:
      print("%.1f m" % (item / 1e0))
    elif item >= 1e-2:
      print("%.1f cm" % (item * 1e2))
    else:
      print("%.1f mm" % (item * 1e3))
else:
  numpy.savetxt(sys.stdout,nfr,fmt='%.6G')
