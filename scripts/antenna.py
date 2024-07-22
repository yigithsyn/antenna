import sys, os, argparse

snme = "ante"                                             # short name
lnme = "antenna"                                          # long name
desc = "Antenna Toolkit"                                  # description
fncs = [                                                  # functions
  {"snme": "util", "lnme": "utility", "desc": "Utility functions"}
]
expl = []                                                 # explanation
frml = []                                                 # formulas 
auth = [                                                  # authors
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = []                                                 # references
parg = []                                                 # positional arguments
oarg = []                                                 # optional arguments
flag = []                                                 # flags

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

# argument parsing 
class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help(sys.stderr)
        exit(2)
pars = ArgumentParser(prog=snme, 
                      description="%s%s%s"%(
                        desc,
                        '\n\nfunctions:\n' if fncs else '','\n'.join(flst)),
                      formatter_class=argparse.RawDescriptionHelpFormatter, 
                      epilog="%s%s%s%s%s%s"%(
                        '\n\nexplanation:\n' if expl else '','\n'.join(expl),
                        '\n\nformula:\n' if frml else '','\n'.join(frml),
                        '\n\nauthor(s):\n' if auth else '','\n'.join(auth)))
args = pars.parse_args(["--help"])