import sys, os, argparse, prettytable
import scipy, numpy

# arguments
tmpl = ""
with open("templates/arguments.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "pnsl"                                   
lnme = "planarNearFieldScanLength"      
desc = "length of associated portion of the scan respect to centerline in planar near-field antenna measurements"
expl.append("Calculation is unitless so output is the same quantity of inputs.")
frml.append("L &= d\\tan\\theta + \\dfrac{a}{2}")
auth.append("Huseyin YIGIT, yigit.hsyn@gmail.com")
refs.append("[1720-2012 - IEEE Recommended Practice for Near-Field Antenna Measurements (p.28 eq.27)](https://ieeexplore.ieee.org/document/6375745)")
parg.append({"name": "d",     "desc": "seperation distance between antenna and probe", "type": float, "cont": 1})
parg.append({"name": "theta", "desc": "desired pattern view angle along one side [deg]",     "type": float, "cont": 1})
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
  inps = numpy.append(inps,[getattr(args,"d"),getattr(args,"theta"),getattr(args,"a")])
inps = numpy.reshape(inps, (-1,3))
inps[:,1] = inps[:,1]/180*numpy.pi
outs = inps[:,0]*numpy.tan(inps[:,1])+inps[:,2]/2

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["antenna-to-probe distance", "view angle [deg]", "cross-section length", "scan length"]
if "--raw" not in sys.argv:
  for i, item in enumerate(outs):
    tabl.add_row(["%.3f"%inps[i][0],"%.1f"%(inps[i][1]*180/numpy.pi),"%.3f"%inps[i][2],"%.3f"%item])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,outs,fmt='%.6G', delimiter="\n")


