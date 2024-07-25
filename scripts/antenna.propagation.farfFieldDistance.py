import sys, os, argparse, prettytable
import scipy, numpy

snme = "ante.prop.ffds"                                   # short name
lnme = "antenna.propagation.farFieldDistance"             # long name
desc = "far-field (Fraunhofer) distance of an antenna or aperture" # description             
fncs = []                                                 # functions
expl = []                                                 # explanation
frml = [                                                  # formulas 
 "R_{ff} &= Max\\left(\\dfrac{2D^2}{\\lambda},5D,1.6\\lambda\\right)"
]
auth = [                                                  # authors
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = [                                                  # references
  "Warren L. Stutzman, Antenna Theory and Design, 3rd Ed., Page 43"
]
parg = [                                                  # positional arguments
  {"name": "frequency", "desc": "frequency of interest in Hz",  "type": float, "cont": 1},
  {"name": "D",         "desc": "maximum cross-sectional size", "type": float, "cont": 1},
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
freq = numpy.asarray([])
clen = numpy.asarray([])
for item in parg:
  args = pars.parse_args(item)
  freq = numpy.append(freq,getattr(args,"frequency"))
  clen = numpy.append(clen,getattr(args,"D"))
wlen = scipy.constants.speed_of_light/freq
ffds = numpy.max([2*numpy.power(clen,2)/clen,5*clen,1.5*wlen], axis=0)

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["frequency [Hz]", "cross-section length [m]", "far-field distance"]
if "--human" in sys.argv:
  for i, item in enumerate(ffds):
    if item >= 1e3:
      pstr = "%.1f km" % (item / 1e3)
    elif item >= 1:
      pstr = "%.1f m" % (item / 1e0)
    elif item >= 1e-2:
      pstr = "%.1f cm" % (item * 1e2)
    else:
      pstr = "%.1f mm" % (item * 1e3)
    tabl.add_row(["%.1f"%freq[i], "%.6f"%clen[i],"%s"%pstr])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,ffds,fmt='%.6G', delimiter="\n")
