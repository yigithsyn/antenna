import sys, os, argparse, prettytable
import math, numpy

# arguments
tmpl = ""
with open("templates/arguments.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "plos"                                   
lnme = "pathLoss"        
desc = "free space path loss under far-field condition"              
expl.append("This calculation valid if two antennas are seperated enough to be inside far-field (Fraunhofer) region.")
frml.append("L_P &= 32.45 + 20\\log10(fR) - G_1 - G_2 \\quad [dB]")
auth.append("Huseyin YIGIT, yigit.hsyn@gmail.com")
parg.append({"name": "frequency", "desc": "frequency of interest in MegaHertz [MHz]", "type": float, "cont": 1})
parg.append({"name": "R",         "desc": "range in kilometers [km]",                 "type": float, "cont": 1})
oarg.append({"name": "G1",        "desc": "gain of transmitter antenna in [dB]",      "type": float, "cont": 1, "dflt": 0})
oarg.append({"name": "G2",        "desc": "gain of receiver    antenna in [dB]",      "type": float, "cont": 1, "dflt": 0})

# prepare arguments
tmpl = ""
with open("templates/prepare_arguments.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

# argument parsing 
tmpl = ""
with open("templates/argument_parsing.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

# implementation
inps = []
for item in parg:
  args = pars.parse_args(item)
  inps = numpy.append(inps,[getattr(args,"frequency"),getattr(args,"R"),[getattr(args,"G1")],[getattr(args,"G2")]])
inps = numpy.reshape(inps, (-1,4))
outs = 32.45 + 20*numpy.log10(inps[:,0]*inps[:,1]) - inps[:,2] - inps[:,3]

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["frequency [MHz]", "ditance [km]", "transmitter antenna gain [dB]", "receiver antenna gain [dB]", "path loss [dB]"]
if "--raw" not in sys.argv:
  for i, item in enumerate(outs):
    tabl.add_row(["%.3f"%inps[i][0],"%.3f"%inps[i][1],"%.1f"%inps[i][2],"%.1f"%inps[i][3],"%.2f"%item])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,outs,fmt='%.6G', delimiter="\n")

