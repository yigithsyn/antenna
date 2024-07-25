import sys, os, argparse, prettytable
import scipy, numpy

tmpl = ""
with open("templates/initials.py", "r") as file:
  tmpl = "".join(file.readlines())
exec(tmpl)

snme = "ante.prop.ffds"                                   
lnme = "antenna.propagation.farFieldDistance"             
desc = "far-field (Fraunhofer) distance of an antenna or aperture"              
frml = [                                                  
 "R_{ff} &= Max\\left(\\dfrac{2D^2}{\\lambda},5D,1.6\\lambda\\right)"
]
auth = [                                                  
  "Huseyin YIGIT, yigit.hsyn@gmail.com"
]
refs = [                                                  
  "Warren L. Stutzman, Antenna Theory and Design, 3rd Ed., Page 43"
]
parg = [                                                  
  {"name": "frequency", "desc": "frequency of interest in Hz",  "type": float, "cont": 1},
  {"name": "D",         "desc": "maximum cross-sectional size", "type": float, "cont": 1},
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
freq = numpy.asarray([])
clen = numpy.asarray([])
for item in parg:
  args = pars.parse_args(item)
  freq = numpy.append(freq,getattr(args,"frequency"))
  clen = numpy.append(clen,getattr(args,"D"))
wlen = scipy.constants.speed_of_light/freq
ffds = numpy.max([2*numpy.power(clen,2)/clen,5*clen,1.5*wlen], axis=0)

# output
tabl = prettytable.PrettyTable()
tabl.set_style(prettytable.MARKDOWN)
tabl.field_names = ["frequency [Hz]", "cross-section length [m]", "far-field distance"]
if "--human" in sys.argv:
  for i, item in enumerate(ffds):
    if item >= 1e3:
      pstr = "%.1f km" % (item / 1e3)
    elif item >= 1:
      pstr = "%.1f m" % (item / 1e0)
    elif item >= 1e-2:
      pstr = "%.1f cm" % (item * 1e2)
    else:
      pstr = "%.1f mm" % (item * 1e3)
    tabl.add_row(["%.1f"%freq[i], "%.6f"%clen[i],"%s"%pstr])
  print("\n%s"%tabl)
else:
  numpy.savetxt(sys.stdout,ffds,fmt='%.6G', delimiter="\n")
