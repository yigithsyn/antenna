import sys, os, argparse
import math

snme = "ante.meas.mren"                                   # short name
lnme = "antenna.measurement.minimumRadiusEnclosed"        # long name
desc = "calculates minimum radius enclosed (MRE) of the antenna for spherical near-field (SNF) measurements" # description             
fncs = []                                                 # functions
expl = [                                                  # explanation
  "Calculation is unitless so output is the same quantity of inputs."
]
frml = [                                                  # formulas 
 "mre &= \\sqrt{dx^2+dy^2+dz^2}"
]
auth = [                                                  # authors
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = []                                                 # references
parg = [                                                  # positional arguments
  {"name": "dx", "desc": "max displacement from rotation center along x-axis", "type": float, "cont": 1},
  {"name": "dy", "desc": "max displacement from rotation center along y-axis", "type": float, "cont": 1},
  {"name": "dz", "desc": "max displacement from rotation center along z-axis", "type": float, "cont": 1}
]
oarg = []                                                 # optional arguments
flag = []                                                 # flags
  
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
        print("error: %s\n"%message)
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
  for line in list(sys.stdin):
    args = pars.parse_args((sys.argv[:1] + line.rstrip().split() + sys.argv[1:])[1:])
    print('%.16G' %(math.sqrt(getattr(args,"dx")[0]**2+getattr(args,"dy")[0]**2+getattr(args,"dz")[0]**2)))
  exit(0)
args = pars.parse_args(sys.argv[1:])

# implementation
print('%.16G' %(math.sqrt(getattr(args,"dx")[0]**2+getattr(args,"dy")[0]**2+getattr(args,"dz")[0]**2)))
