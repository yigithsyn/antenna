import sys, os, argparse

tmpl = ""
with open("templates/initials.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "ante.meas"                                        
lnme = "antenna.measurement"                              
desc = "Antenna Measurement support functions"            
fncs = [                                                  
  {"snme": "mnfr", "lnme": "miniumumNearFieldRange",  "desc": "minimum recommended distance for near-field antenna measurements"},
  {"snme": "mren", "lnme": "minimumRadiusEnclosed",   "desc": "calculates minimum radius enclosed (MRE) of the antenna for spherical near-field (SNF) measurements"},
  {"snme": "nfps", "lnme": "nearFieldPlanarSampling", "desc": "near-field planar antenna measurement sampling count"},
  {"snme": "nfsl", "lnme": "nearFieldSamplingLength", "desc": "minimum sampling distance for near-field antenna measurements"},
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
flst = []                                                 
for i in range(len(fncs)):
  flst.append("  %s: %s"%(fncs[i]["lnme"].ljust(25),fncs[i]["desc"]))
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