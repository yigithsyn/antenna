import sys, os, argparse, prettytable
import scipy, numpy

# arguments
tmpl = ""
with open("templates/arguments.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "fr2w"                                   
lnme = "frequencyToWavelength"            
desc = "frequency to wavelength conversion"               
frml.append("\\lambda &= c0/f")
auth.append("Huseyin YIGIT, yigit.hsyn@gmail.com")
parg.append({"name": "frequency", "desc": "frequency in Hertz [Hz]", "type": float, "cont": "+"})

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
out0 = []
inp0 = []
for item in parg:
  args = pars.parse_args(item)
  inp0.append(getattr(args,"frequency"))
out0 = scipy.constants.speed_of_light / numpy.asarray(inp0)

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["Frequency [Hz]", "Wavelength",]
if "--raw" not in sys.argv:
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
  numpy.savetxt(sys.stdout,out0,fmt='%.16G',delimiter="\n")


