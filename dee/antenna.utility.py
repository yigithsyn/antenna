import sys, os, argparse

snme = "ante.util"                                        
lnme = "antenna.utility"                                  
desc = "Utility functions"                                
fncs = [                                                  
  {"snme": "fr2w", "lnme": "frequencyToWavelength", "desc": "frequency to wavelength conversion"}
.append({"snme": "wl2f", "lnme": "wavelengthToFrequency", "desc": "wavelength to frequency conversion"}
.append({"snme": "gm2s", "lnme": "gammaToSwr",            "desc": "reflection coefficient (gamma) to voltage standing wave ratio (vswr) conversion"}
.append({"snme": "sw2g", "lnme": "swrToGamma",            "desc": "voltage standing wave ratio (vswr) to reflection coefficient (gamma) conversion"})
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