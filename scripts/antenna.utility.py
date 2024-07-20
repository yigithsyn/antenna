import sys, os
from argparse import ArgumentParser, RawDescriptionHelpFormatter

snme = "ante.util"                                        # short name
lnme = "antenna.utility"                                  # long name
desc = "Utility functions"                                # description
fncs = [                                                  # functions
  {"snme": "fr2w", "lnme": "frequencyToWavelength", "desc": "frequency to wavelength conversion"},
  {"snme": "wl2f", "lnme": "wavelengthToFrequency", "desc": "wavelength to frequency conversion"},
  {"snme": "gm2s", "lnme": "gammaToSwr",            "desc": "reflection coefficient (gamma) to voltage standing wave ratio (vswr) conversion"}
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
args = pars.parse_args(["--help"])