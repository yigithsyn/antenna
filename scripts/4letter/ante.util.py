from sys import argv
from argparse import ArgumentParser, RawDescriptionHelpFormatter

pars = ArgumentParser(prog="ante.util", description="Utility functions", formatter_class=RawDescriptionHelpFormatter, epilog="functions:\n  fr2w: frequency to wavelength conversion\n  gm2s: reflection coefficient (gamma) to voltage standing wave ratio (vswr) conversion\n  wl2f: wavelength to frequency conversion\n\nauthor(s):\n  Huseyin YIGIT, yigit.hsyn@gmail.com")
args = pars.parse_args(["--help"])