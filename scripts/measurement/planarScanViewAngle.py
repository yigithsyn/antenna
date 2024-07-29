import sys, os, argparse, prettytable
import scipy, numpy

# arguments
tmpl = ""
with open("templates/arguments.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "plva"                                   
lnme = "planarScanViewAngle"      
desc = "pattern view angle along one side"              
expl.append("Calculation is unitless so output is the same quantity of inputs.")
frml.append("\\theta = \\tan^{-1}\\left(\\frac{L - \\dfrac{a}{2}}{d}\\right)")
auth.append("Huseyin YIGIT, yigit.hsyn@gmail.com")
parg.append({"name": "L",     "desc": "length of associated portion of the scan respect to centerline",     "type": float, "cont": 1})
parg.append({"name": "d",     "desc": "seperation distance between antenna and probe", "type": float, "cont": 1})
parg.append({"name": "a",     "desc": "antenna cross-section length",                  "type": float, "cont": 1})
  
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
  inps = numpy.append(inps,[getattr(args,"L"),getattr(args,"d"),getattr(args,"a")])
inps = numpy.reshape(inps, (-1,3))
outs = numpy.atan2((inps[:,0]-inps[:,2]/2),inps[:,1])*180/numpy.pi

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["scan length (L)", "antenna-to-probe (d)", "cross-section length (a)", "view angle [deg]"]
if "--raw" not in sys.argv:
  for i, item in enumerate(outs):
    tabl.add_row(["%.3f"%inps[i][0],"%.3f"%inps[i][1],"%.3f"%inps[i][2],"%.1f"%item])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,outs,fmt='%.6G', delimiter="\n")


