import sys, os
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import scipy
import numpy

snme = "ante.util.gm2s"                                   # short name
lnme = "antenna.utility.gammaToSwr"                       # long name
desc = "reflection coefficient (gamma) to voltage standing wave ratio (vswr) conversion" # description             
fncs = []                                                 # functions
expl = []                                                 # explanation
frml = [                                                  # formulas 
 "SWR &= \\dfrac{1+|\\Gamma|}{1-|\\Gamma|}"
]
auth = [                                                  # authors
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = [                                                  # references
  "https://en.wikipedia.org/wiki/Reflection_coefficient",
  "https://en.wikipedia.org/wiki/Standing_wave_ratio"
]
parg = [                                                  # positional arguments
  {"name": "gamma", "desc": "reflection coefficient", "type": float, "cont": 1}
]
oarg = []                                                 # optional arguments
flag = [                                                  # flags
  {"name": "db", "desc": "input reflection coefficient in dB"}
]

# preparation for parsing 
flst = []
for i in range(len(fncs)):
  flst.append("  %s: %s"%(fncs[i]["snme"].ljust(4),fncs[i]["desc"]))
for i in range(len(frml)):
  frml[i] = "  " + frml[i]
for i in range(len(auth)):
  auth[i] = "  " + auth[i]
for i in range(len(refs)):
  refs[i] = "  - " + refs[i]

# argument parsing 
pars = ArgumentParser(prog=snme, 
                      description="%s%s%s"%(
                        desc,
                        '\n\nfunctions:\n' if fncs else '','\n'.join(flst)),
                      formatter_class=RawDescriptionHelpFormatter, 
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
  for line in sys.stdin:
    sys.argv = sys.argv[:1] + [line] + sys.argv[1:]
args = pars.parse_args(sys.argv[1:])

# implementation
vswr = numpy.power(10,numpy.asarray(getattr(args,"gamma"),dtype="float")/20) if getattr(args,"db") else numpy.asarray(getattr(args,"gamma"),dtype="float") 
numpy.savetxt(sys.stdout,(1+vswr)/(1-vswr),fmt='%.3G')