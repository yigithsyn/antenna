import sys, os, argparse, prettytable
import scipy, math

snme = "ante.meas.nfsc"                                   # short name
lnme = "antenna.measurement.nearFieldSamplingCount"       # long name
desc = "near-field antenna measurement sampling count"    # description             
fncs = []                                                 # functions
expl = [                                                  # explanation
  "function returns following outputs respectively:",
  "  calculated sampling length",
  "  sampling start position (zero centered)",
  "  sampling finish position (zero centered)",
  "  sampling count"
]
frml = []                                                 # formulas 
auth = [                                                  # authors
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = []                                                 # references
parg = [                                                  # positional arguments
  {"name": "frequency", "desc": "frequency of interest in Hertz [Hz]",           "type": float, "cont": 1},
  {"name": "length",    "desc": "initial desired sampling length in meters [m]", "type": float, "cont": 1},
]
oarg = []                                                 # optional arguments
flag = [                                                  # flags
  {"name": "human", "desc": "human readable tabulated output"}
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
outs = []
for item in parg:
  args = pars.parse_args(item)
  nfsl = math.floor(0.5*scipy.constants.speed_of_light/getattr(args,"frequency")[0]*1E3)
  slen = math.ceil(getattr(args,"length")[0]*1E3)
  slen = slen/2 if slen%2==0 else (slen+1)/2
  if slen%nfsl > 0:
    slen = slen + (nfsl-slen%nfsl)
  outs.append([nfsl,-float(slen)/1000,+float(slen)/1000,2*(slen/nfsl)+1])

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["Frequency [Hz]", "Desired Length [m]", "Sampling Length [mm]", "Scan Start [m]", "Scan End [m]", "Sampling Count"]
if "--human" in sys.argv:
  for i in range(len(outs)):
    tabl.add_row(["%s"%parg[i][0],"%s"%parg[i][1], "%d"%outs[i][0],"%.3f"%outs[i][1],"%.3f"%outs[i][2],"%d"%outs[i][3]])
  print("\n%s"%tabl)
else:
  print('%d %.3f %.3f %d'%(outs[-1][0],outs[-1][1],outs[-1][2],outs[-1][3]))

