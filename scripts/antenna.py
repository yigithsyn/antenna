import sys, os, argparse

tmpl = ""
with open("templates/initials.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "ante"                                             
lnme = "antenna"                                          
desc = "Antenna Toolkit"                                  
fncs = [                                                  
  {"snme": "util", "lnme": "utility",     "desc": "Utility functions"},
  {"snme": "meas", "lnme": "measurement", "desc": "Measurement support functions"}
]
auth = [                                                  
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]

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