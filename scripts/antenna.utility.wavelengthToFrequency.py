import sys, os, argparse, prettytable
import scipy
import numpy

tmpl = ""
with open("templates/initials.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "ante.util.wl2f"                                   
lnme = "antenna.utility.wavelengthToFrequency"            
desc = "wavelength to frequency conversion"               
frml = [                                                  
  "f &= c0/\\lambda"
]
auth = [                                                  
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
parg = [                                                  
  {"name": "wavelength", "desc": "wavelength in meters [m]", "type": float, "cont": "+"}
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
  inp0.append(getattr(args,"wavelength"))
out0 = scipy.constants.speed_of_light / numpy.asarray(inp0)

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["Wavelength [m]", "Frequency",]
if "--human" in sys.argv:
  for i in range(len(out0)):
    for j in range(len(out0[i])):
      if (out0[i][j] >= 1E12):
        pstr = '%.1f THz'%(out0[i][j] / 1E12)
      elif (out0[i][j] >= 1E9):
        pstr = '%.1f GHz'%(out0[i][j] / 1E9)
      elif (out0[i][j] >= 1E6):
        pstr = '%.1f MHz'%(out0[i][j] / 1E6)
      elif (out0[i][j] >= 1E3):
        pstr = '%.1f kHz' %(out0[i][j]/1E3)
      else:
        pstr = '%.1f Hz' %(out0[i][j]/1E3)
      tabl.add_row(["%s"%parg[i][j],"%s"%pstr])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,out0,fmt='%.1G',delimiter="\n")

