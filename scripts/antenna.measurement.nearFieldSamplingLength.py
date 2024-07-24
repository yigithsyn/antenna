import sys, os, argparse, prettytable
import scipy, numpy

snme = "ante.meas.nfsl"                                   # short name
lnme = "antenna.measurement.nearFieldSamplingLength"      # long name
desc = "minimum sampling distance for near-field antenna measurements" # description             
fncs = []                                                 # functions
expl = []                                                 # explanation
frml = [                                                  # formulas 
 "\\Delta &= \\lambda/2 = c_0/(2\\timesf)"
]
auth = [                                                  # authors
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = []                                                 # references
parg = [                                                  # positional arguments
  {"name": "frequency", "desc": "frequency of interest in Hertz [Hz]", "type": float, "cont": "+"}
]
oarg = []                                                 # optional arguments
flag = [                                                  # flags
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
  inp0.append(getattr(args,"frequency"))
out0 = 0.5*scipy.constants.speed_of_light / numpy.asarray(inp0, dtype="float")

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["Frequency [Hz]", "Sampling Length",]
if "--human" in sys.argv:
  for i in range(len(out0)):
    for j in range(len(out0[i])):
      if out0[i][j] >= 1e3:
        pstr = "%.1f km" % (out0[i][j] / 1e3)
      elif out0[i][j] >= 1:
        pstr = "%.1f m" % (out0[i][j] / 1e0)
      elif out0[i][j] >= 1e-2:
        pstr = "%.1f cm" % (out0[i][j] * 1e2)
      else:
        pstr = "%.1f mm" % (out0[i][j] * 1e3)
      tabl.add_row(["%s"%parg[i][j],"%s"%pstr])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,out0,fmt='%.6G',delimiter="\n")
