import sys, os, argparse, prettytable
import scipy
import numpy

tmpl = ""
with open("templates/initials", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "ante.meas.mnfr"                                   
lnme = "antenna.measurement.miniumumNearFieldRange"       
desc = "minimum recommended distance for near-field antenna measurements in meters"              
expl = [                                                  
  "Standard suggests to choose between 3 or 5 wavelength.",
  "In order to ensure copuling effect, 5 wavelength distance is choosen and implemented."
]
frml = [                                                  
 "R_{nf} &= 5\\times\\lambda = 5\\times c_0/f"
]
auth = [                                                  
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = [                                                  
  "[IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.3.1.4, Page 27](https://ieeexplore.ieee.org/document/6375745)",
]
parg = [                                                  
  {"name": "frequency", "desc": "frequency of interest in Hertz [Hz]", "type": float, "cont": "+"}
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
  inp0.append(getattr(args,"frequency"))
out0 = 5*scipy.constants.speed_of_light/numpy.asarray(inp0)

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["Frequency [Hz]", "Near-field Starting Range"]
if "--human" in sys.argv:
  for i in range(len(out0)):
    for j in range(len(out0[i])):
      if out0[i][j] >= 1e3:
        pstr = "%.1f km" % (out0[i][j] / 1e3)
      elif out0[i][j] >= 1:
        pstr = "%.1f m" % (out0[i][j] / 1e0)
      elif out0[i][j] >= 1e-2:
        pstr = "%.1f cm" % (out0[i][j] * 1e2)
      else:
        pstr = "%.1f mm" % (out0[i][j] * 1e3)
      tabl.add_row(["%s"%parg[i][j],"%s"%pstr])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,out0,fmt='%.6G', delimiter="\n")
