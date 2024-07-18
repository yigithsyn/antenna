from sys import argv
from argparse import ArgumentParser, RawDescriptionHelpFormatter

pars = ArgumentParser(prog="antenna", description="Antenna Toolkit", formatter_class=RawDescriptionHelpFormatter, epilog="functions:\n  util: Utility functions\n\nauthor(s):\n  Huseyin YIGIT, yigit.hsyn@gmail.com")
args = pars.parse_args(["--help"])