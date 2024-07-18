from sys import argv
from argparse import ArgumentParser, RawDescriptionHelpFormatter

pars = ArgumentParser(prog="antenna.utility", description="Utility functions", formatter_class=RawDescriptionHelpFormatter, epilog="functions:\n  frequencyToWavelength: frequency to wavelength conversion\n  gammaToSwr: reflection coefficient (gamma) to voltage standing wave ratio (vswr) conversion\n  wavelengthToFrequency: wavelength to frequency conversion\n\nauthor(s):\n  Huseyin YIGIT, yigit.hsyn@gmail.com")
args = pars.parse_args(["--help"])