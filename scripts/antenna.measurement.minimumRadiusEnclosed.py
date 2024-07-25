import sys, os, argparse, prettytable
import math, numpy

tmpl = ""
with open("templates/initials.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)


snme = "ante.meas.mren"                                   
lnme = "antenna.measurement.minimumRadiusEnclosed"        
desc = "calculates minimum radius enclosed (MRE) of the antenna for spherical near-field (SNF) measurements"              
expl = [                                                  
  "Calculation is unitless so output is the same quantity of inputs."
]
frml = [                                                  
 "mre &= \\sqrt{dx^2+dy^2+dz^2}"
]
auth = [                                                  
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
parg = [                                                  
  {"name": "dx", "desc": "max displacement from rotation center along x-axis", "type": float, "cont": 1},
  {"name": "dy", "desc": "max displacement from rotation center along y-axis", "type": float, "cont": 1},
  {"name": "dz", "desc": "max displacement from rotation center along z-axis", "type": float, "cont": 1}
]
flag = [                                                  
  {"name": "human", "desc": "human readable output"}
]

# argument parsing 
tmpl = ""
with open("templates/argument_parsing.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

# implementation
out0 = []
inp0 = []
for item in parg:
  args = pars.parse_args(item)
  out0.append([math.sqrt(getattr(args,"dx")[0]**2+getattr(args,"dy")[0]**2+getattr(args,"dz")[0]**2)])

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["dx", "dy", "dz", "MRE"]
if "--human" in sys.argv:
  for i in range(len(out0)):
    for j in range(len(out0[i])):
      tabl.add_row(["%s"%parg[i][0],"%s"%parg[i][1],"%s"%parg[i][2],"%.3f"%out0[i][j]])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,out0,fmt='%.6G', delimiter="\n")
