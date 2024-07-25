import sys, os, argparse

snme = "ante.util"                                        
lnme = "antenna.utility"                                  
desc = "Utility functions"                                
fncs = [                                                  
  {"snme": "fr2w", "lnme": "frequencyToWavelength", "desc": "frequency to wavelength conversion"},
  {"snme": "wl2f", "lnme": "wavelengthToFrequency", "desc": "wavelength to frequency conversion"},
  {"snme": "gm2s", "lnme": "gammaToSwr",            "desc": "reflection coefficient (gamma) to voltage standing wave ratio (vswr) conversion"},
  {"snme": "sw2g", "lnme": "swrToGamma",            "desc": "voltage standing wave ratio (vswr) to reflection coefficient (gamma) conversion"}
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