import sys, os, argparse, prettytable
import math, numpy

snme = "ante.meas.mren"                                   
lnme = "antenna.measurement.minimumRadiusEnclosed"        
desc = "calculates minimum radius enclosed (MRE) of the antenna for spherical near-field (SNF) measurements"              
fncs = []                                                 
expl = [                                                  
  "Calculation is unitless so output is the same quantity of inputs."
]
frml = [                                                  
 "mre &= \\sqrt{dx^2+dy^2+dz^2}"
]
auth = [                                                  
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = []                                                 
parg = [                                                  
  {"name": "dx", "desc": "max displacement from rotation center along x-axis", "type": float, "cont": 1},
  {"name": "dy", "desc": "max displacement from rotation center along y-axis", "type": float, "cont": 1},
  {"name": "dz", "desc": "max displacement from rotation center along z-axis", "type": float, "cont": 1}
]
oarg = []                                                 
flag = [                                                  
  {"name": "human", "desc": "human readable output"}
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
parg = [] 
if not os.isatty(sys.stdin.fileno()):
  for line in list(sys.stdin):
    parg.append(line.rstrip().split() + list(filter(lambda item: '-' in item or '--' in item, sys.argv[1:])))
    pars.parse_args(parg[-1])
else:
  parg.append(sys.argv[1:])
  pars.parse_args(parg[-1])

# implementation
out0 = []
inp0 = []
for item in parg:
  args = pars.parse_args(item)
  out0.append([math.sqrt(getattr(args,"dx")[0]**2+getattr(args,"dy")[0]**2+getattr(args,"dz")[0]**2)])

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["dx", "dy", "dz", "MRE"]
if "--human" in sys.argv:
  for i in range(len(out0)):
    for j in range(len(out0[i])):
      tabl.add_row(["%s"%parg[i][0],"%s"%parg[i][1],"%s"%parg[i][2],"%.3f"%out0[i][j]])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,out0,fmt='%.6G', delimiter="\n")
