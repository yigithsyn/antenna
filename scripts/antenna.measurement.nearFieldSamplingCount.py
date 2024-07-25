import sys, os, argparse, prettytable
import scipy, math

# definitions
# arguments
tmpl = ""
with open("templates/arguments.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "ante.meas.nfps"                                   
lnme = "antenna.measurement.nearFieldPlanarSampling"      
desc = "near-field planar antenna measurement sampling count"                 
expl.append("function returns following outputs respectively:")
expl.append("  calculated sampling length")
expl.append("  sampling start position (zero centered)")
expl.append("  sampling finish position (zero centered)")
expl.append("  sampling count")
auth.append("Huseyin YIGIT, yigit.hsyn@gmail.com")
parg.append({"name": "frequency", "desc": "frequency of interest in Hertz [Hz]",           "type": float, "cont": 1})
parg.append({"name": "length",    "desc": "initial desired sampling length in meters [m]", "type": float, "cont": 1})
flag.append({"name": "human", "desc": "human readable output"})

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
outs = []
for item in parg:
  args = pars.parse_args(item)
  nfsl = math.floor(0.5*scipy.constants.speed_of_light/getattr(args,"frequency")[0]*1E3)
  slen = math.ceil(getattr(args,"length")[0]*1E3)
  slen = slen/2 if slen%2==0 else (slen+1)/2
  if slen%nfsl > 0:
    slen = slen + (nfsl-slen%nfsl)
  outs.append([nfsl,-float(slen)/1000,+float(slen)/1000,2*(slen/nfsl)+1])

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["Frequency [Hz]", "Desired Length [m]", "Sampling Length [mm]", "Scan Start [m]", "Scan End [m]", "Sampling Count"]
if "--human" in sys.argv:
  for i in range(len(outs)):
    tabl.add_row(["%s"%parg[i][0],"%s"%parg[i][1], "%d"%outs[i][0],"%.3f"%outs[i][1],"%.3f"%outs[i][2],"%d"%outs[i][3]])
  print("\n%s"%tabl)
else:
  print('%d %.3f %.3f %d'%(outs[-1][0],outs[-1][1],outs[-1][2],outs[-1][3]))

