import sys, os
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import scipy
import numpy

snme = "ante.util.fr2w"                                   # short name
lnme = "antenna.utility.frequencyToWavelength"            # long name
desc = "frequency to wavelength conversion"               # description
fncs = []                                                 # functions
expl = []                                                 # explanation
frml = [                                                  # formulas 
  "\\lambda &= c0/f"
]
auth = [                                                  # authors
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = []                                                 # references
parg = [                                                  # positional arguments
  {"name": "frequency", "desc": "frequency in Hertz [Hz]", "type": float, "cont": 1}
]
oarg = []                                                 # optional arguments
flag = [                                                  # flags
  {"name": "human", "desc": "human readable output like cm, mm, km"}
]

# preparation for parsing 
flst = []
for i in range(len(fncs)):
  flst.append("  %s: %s"%(fncs[i]["snme"].ljust(4),fncs[i]["desc"]))
for i in range(len(frml)):
  frml[i] = "  " + frml[i]
for i in range(len(auth)):
  auth[i] = "  " + auth[i]

# argument parsing 
pars = ArgumentParser(prog=snme, 
                      description="%s%s%s"%(
                        desc,
                        '\n\nfunctions:\n' if fncs else '','\n'.join(flst)),
                      formatter_class=RawDescriptionHelpFormatter, 
                      epilog="%s%s%s%s%s%s"%(
                        '\n\nexplanation:\n' if expl else '','\n'.join(expl),
                        '\n\nformula:\n' if frml else '','\n'.join(frml),
                        '\n\nauthor(s):\n' if auth else '','\n'.join(auth)))
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
wlen = scipy.constants.speed_of_light / numpy.asarray(getattr(args,"frequency"), dtype="float")
for item in wlen:
  if getattr(args,"human"):
    if item >= 1e3:
      print("%.1f km" % (item / 1e3))
    elif item >= 1:
      print("%.1f m" % (item / 1e0))
    elif item >= 1e-2:
      print("%.1f cm" % (item * 1e2))
    else:
      print("%.1f mm" % (item * 1e3))
  else:
    print("%.16G" % (item))
