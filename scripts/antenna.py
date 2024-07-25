import sys, os, argparse

snme = "ante"                                             
lnme = "antenna"                                          
desc = "Antenna Toolkit"                                  
fncs = [                                                  
  {"snme": "util", "lnme": "utility",     "desc": "Utility functions"},
  {"snme": "meas", "lnme": "measurement", "desc": "Measurement support functions"}
]
expl = []                                                 
frml = []                                                 
auth = [                                                  
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = []                                                 
parg = []                                                 
oarg = []                                                 
flag = []                                                 

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
                      epilog="%s%s%s%s%s%s"%(
                        '\n\nexplanation:\n' if expl else '','\n'.join(expl),
                        '\n\nformula:\n' if frml else '','\n'.join(frml),
                        '\n\nauthor(s):\n' if auth else '','\n'.join(auth)))
args = pars.parse_args(["--help"])