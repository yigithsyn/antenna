import sys, os, argparse, prettytable
import numpy

tmpl = ""
with open("templates/initials.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "ante.util.sw2g"                                   
lnme = "antenna.utility.swrToGamma"                       
desc = "voltage standing wave ratio (vswr) to reflection coefficient (gamma) conversion"              
frml = [                                                  
 "\\Gamma &= \\dfrac{1-SWR}{1+SWR}"
]
auth = [                                                  
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = [                                                  
  "[Reflection coefficient - Wikipedia](https://en.wikipedia.org/wiki/Reflection_coefficient)",
  "[Standing wave ratio - Wikipedia](https://en.wikipedia.org/wiki/Standing_wave_ratio)"
]
parg = [                                                  
  {"name": "swr", "desc": "standing wave ratio", "type": float, "cont": "+"}
]
flag = [                                                  
  {"name": "db",    "desc": "output reflection coefficient in dB"},
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
  inp0.append(getattr(args,"swr"))
out0 = (numpy.asarray(inp0)-1)/(numpy.asarray(inp0)+1)
out0 = 20*numpy.log10(out0) if "--db" in sys.argv else out0

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["(V)SWR", "Gamma (S11)"+(" [dB]"if "--db" in sys.argv else "")]
if "--human" in sys.argv:
  for i in range(len(out0)):
    for j in range(len(out0[i])):
      tabl.add_row(["%s"%parg[i][j],"%.3f"%out0[i][j]])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,out0,fmt='%.3G', delimiter="\n")
