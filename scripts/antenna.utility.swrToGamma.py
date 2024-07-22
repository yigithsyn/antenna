import sys, os
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import scipy
import numpy

snme = "ante.util.sw2g"                                   # short name
lnme = "antenna.utility.swrToGamma"                       # long name
desc = "voltage standing wave ratio (vswr) to reflection coefficient (gamma) conversion" # description             
fncs = []                                                 # functions
expl = []                                                 # explanation
frml = [                                                  # formulas 
 "\\Gamma &= \\dfrac{1-SWR}{1+SWR}"
]
auth = [                                                  # authors
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = [                                                  # references
  "[Reflection coefficient - Wikipedia](https://en.wikipedia.org/wiki/Reflection_coefficient)",
  "[Standing wave ratio - Wikipedia](https://en.wikipedia.org/wiki/Standing_wave_ratio)"
]
parg = [                                                  # positional arguments
  {"name": "swr", "desc": "standing wave ratio", "type": float, "cont": "+"}
]
oarg = []                                                 # optional arguments
flag = [                                                  # flags
  {"name": "db", "desc": "output reflection coefficient in dB"}
]

# preparation for parsing 
flst = []
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
  for line in reversed(list(sys.stdin)):
    sys.argv = sys.argv[:1] + [line.rstrip()] + sys.argv[1:]
args = pars.parse_args(sys.argv[1:])

# implementation
gmml = (numpy.asarray(getattr(args,"swr"))-1)/(numpy.asarray(getattr(args,"swr"))+1)
numpy.savetxt(sys.stdout,(20*numpy.log10(gmml) if getattr(args,"db") else gmml),fmt='%.03G')