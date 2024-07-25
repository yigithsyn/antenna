import sys, os, argparse, prettytable
import scipy, numpy

# arguments
tmpl = ""
with open("templates/arguments.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "losd"                                   
lnme = "lineOfSightDistance"             
desc = "line-of-sight range in kilometers [km] for a given height"              
frml.append("R_{los} &= \\sqrt{2\\cdotR\\cdoth} \\approx 3.57\\times\\sqrt{h} [km]")
auth.append("Huseyin YIGIT, yigit.hsyn@gmail.com")
refs.append("[Line-of-sight propagation - Wikipedia](https://en.wikipedia.org/wiki/Line-of-sight_propagation)")
parg.append({"name": "height", "desc": "height of transmitter/recevier above ground in meters [m]",  "type": float, "cont": "+"})
flag.append({"name": "human",  "desc": "human readable output"})
  
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
inps = numpy.asarray([])
outs = numpy.asarray([])
i = numpy.asarray([])
for item in parg:
  args = pars.parse_args(item)
  inps = numpy.append(inps,getattr(args,"height"))
outs = 3.57*numpy.sqrt(inps)

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["height [m]", "line-of-light distance [km]"]
if "--human" in sys.argv:
  for i, item in enumerate(outs):
    tabl.add_row(["%.3f"%inps[i], "%.6f"%item])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,outs,fmt='%.6f', delimiter="\n")
