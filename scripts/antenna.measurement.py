import sys, os, argparse

# definitions
# arguments
tmpl = ""
with open("templates/arguments.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "ante.meas"                                        
lnme = "antenna.measurement"                              
desc = "Antenna Measurement support functions"            
fncs = [                                                  
  {"snme": "mnfr", "lnme": "miniumumNearFieldRange",  "desc": "minimum recommended distance for near-field antenna measurements"}
.append({"snme": "mren", "lnme": "minimumRadiusEnclosed",   "desc": "calculates minimum radius enclosed (MRE) of the antenna for spherical near-field (SNF) measurements"}
.append({"snme": "nfps", "lnme": "nearFieldPlanarSampling", "desc": "near-field planar antenna measurement sampling count"}
.append({"snme": "nfsl", "lnme": "nearFieldSamplingLength", "desc": "minimum sampling distance for near-field antenna measurements"}})
auth.append("Huseyin YIGIT, yigit.hsyn@gmail.com")

# prepare arguments
tmpl = ""
with open("templates/prepare_arguments.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

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