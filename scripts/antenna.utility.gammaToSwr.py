import sys, os, argparse, prettytable
import numpy

tmpl = ""
with open("templates/initials.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "ante.util.gm2s"                                   
lnme = "antenna.utility.gammaToSwr"                       
desc = "reflection coefficient (gamma) to voltage standing wave ratio (vswr) conversion"              
frml = [                                                  
 "SWR &= \\dfrac{1+|\\Gamma|}{1-|\\Gamma|}"
]
auth = [                                                  
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = [                                                  
  "[Reflection coefficient - Wikipedia](https://en.wikipedia.org/wiki/Reflection_coefficient)",
  "[Standing wave ratio - Wikipedia](https://en.wikipedia.org/wiki/Standing_wave_ratio)"
]
parg = [                                                  
  {"name": "gamma", "desc": "reflection coefficient", "type": float, "cont": "+"}
]
flag = [                                                  
  {"name": "db",    "desc": "input reflection coefficient in dB"},
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
  inp0.append(getattr(args,"gamma"))
out0 = numpy.power(10,numpy.asarray(inp0)/20) if "--db" in sys.argv else numpy.asarray(inp0)
out0 = (1+out0)/(1-out0)

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["Gamma (S11)"+(" [dB]"if "--db" in sys.argv else ""), "(V)SWR"]
if "--human" in sys.argv:
  for i in range(len(out0)):
    for j in range(len(out0[i])):
      tabl.add_row(["%s"%parg[i][j],"%.3f"%out0[i][j]])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,out0,fmt='%.3G', delimiter="\n")
