import sys, os, argparse, prettytable
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
  {"name": "db",    "desc": "output reflection coefficient in dB"},
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
  inp0.append(getattr(args,"swr"))
out0 = (numpy.asarray(inp0)-1)/(numpy.asarray(inp0)+1)
out0 = 20*numpy.log10(out0) if "--db" in sys.argv else out0

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["(V)SWR", "Gamma (S11)"+(" [dB]"if "--db" in sys.argv else "")]
if "--human" in sys.argv:
  for i in range(len(out0)):
    for j in range(len(out0[i])):
      tabl.add_row(["%s"%parg[i][j],"%.3f"%out0[i][j]])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,out0,fmt='%.3G', delimiter="\n")
