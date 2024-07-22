import sys
import argparse
 
if len(sys.argv)>1 and sys.argv[1] == "freq2wlen":
	parser = argparse.ArgumentParser(prog="freq2wlen", description="frequency to wavelength conversion", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="formula:\n\\\\lambda &= c0/f\n\n")
	parser.add_argument("freq", help="frequency in Hertz [Hz]", type=float, nargs=1)
	parser.add_argument("--human", help="human readable output like cm, mm, km", action="store_true")
	args = parser.parse_args(sys.argv[2:])
	import scipy.constants as constants
	wle = constants.speed_of_light/args.freq[0]
	if args.human: 
		if (wle >= 1E3):
			print('%.1f km'%(wle / 1E3))
		elif (wle >= 1):
			print('%.1f m'%(wle / 1E0))
		elif (wle >= 1E-2):
			print('%.1f cm'%(wle * 1E2))
		else:
			print('%.1f mm' %(wle*1E3))
	else:
		print('%.16G' %(wle))
elif len(sys.argv)>1 and sys.argv[1] == "gamma2swr":
	parser = argparse.ArgumentParser(prog="gamma2swr", description="reflection coefficient (gamma) to standing wave ratio (swr) conversion", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="formula:\nSWR &= \\\\dfrac{1+|\\\\Gamma|}{1-|\\\\Gamma|}\n\nreferences:\n- [Reflection coefficient - Wikipedia](https://en.wikipedia.org/wiki/Reflection_coefficient)\n- [Standing wave ratio - Wikipedia](https://en.wikipedia.org/wiki/Standing_wave_ratio)")
	parser.add_argument("gamma", help="reflection coefficient", type=float, nargs="+")
	parser.add_argument("--db", help="input reflection coefficient in dB", action="store_true")
	args = parser.parse_args(sys.argv[2:])
	import numpy
	gml = numpy.power(10,numpy.asarray(args.gamma)/20) if args.db else numpy.asarray(args.gamma)
	numpy.set_printoptions(precision=3)
	numpy.savetxt(sys.stdout,(1+gml)/(1-gml),fmt='%.16G')
elif len(sys.argv)>1 and sys.argv[1] == "swr2gamma":
	parser = argparse.ArgumentParser(prog="swr2gamma", description="standing wave ratio (swr) to reflection coefficient (gamma) conversion", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="formula:\n\\\\Gamma &= \\\\dfrac{1-SWR}{1+SWR}\n\nreferences:\n- [Reflection coefficient - Wikipedia](https://en.wikipedia.org/wiki/Reflection_coefficient)\n- [Standing wave ratio - Wikipedia](https://en.wikipedia.org/wiki/Standing_wave_ratio)")
	parser.add_argument("swr", help="standing wave ration", type=float, nargs="+")
	parser.add_argument("--db", help="output reflection coefficient in dB", action="store_true")
	args = parser.parse_args(sys.argv[2:])
	import numpy
	gml = (numpy.asarray(args.swr)-1)/(numpy.asarray(args.swr)+1)
	numpy.set_printoptions(precision=3)
	numpy.savetxt(sys.stdout,(20*numpy.log10(gml) if args.db else gml),fmt='%.16G')
elif len(sys.argv)>1 and sys.argv[1] == "wlen2freq":
	parser = argparse.ArgumentParser(prog="wlen2freq", description="wavelength to frequency conversion", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="formula:\nf &= c0/\\\\lambda\n\n")
	parser.add_argument("wlen", help="wavelength in meters [m]", type=float, nargs=1)
	parser.add_argument("--human", help="human readable output like kHz, MHz, GHz", action="store_true")
	args = parser.parse_args(sys.argv[2:])
	import scipy.constants as constants
	frq = constants.speed_of_light/args.wlen[0] 
	if args.human:
		if (frq >= 1E12):
			print('%.1f THz'%(frq / 1E12))
		elif (frq >= 1E9):
			print('%.1f GHz'%(frq / 1E9))
		elif (frq >= 1E6):
			print('%.1f MHz'%(frq / 1E6))
		elif (frq >= 1E3):
			print('%.1f kHz' %(frq/1E3))
		else:
			print('%.1f Hz' %(frq))
	else:
		print('%.16G' %(frq))
elif len(sys.argv)>1 and sys.argv[1] == "measurement":
	if len(sys.argv)>2 and sys.argv[2] == "nfrange":
		parser = argparse.ArgumentParser(prog="nfrange", description="minimum recommended distance for near-field antenna measurements", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n\nformula:\nR_{nf} &= 5\\times\\lambda = 5\\times c_0/f\n\nreferences:\n- IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.3.1.4, Page 27")
		parser.add_argument("freq", help="frequency of interest in Hertz [Hz]", type=float, nargs="+")
		parser.add_argument("--human", help="human readable output like mm, cm, m", action="store_true")
		args = parser.parse_args(sys.argv[3:])
		import scipy.constants as constants
		nfr = 3*constants.speed_of_light/args.freq[0]
		if args.human: 
			if (nfr >= 1E3):
				print('%.1f km'%(nfr / 1E3))
			elif (nfr >= 1):
				print('%.1f m'%(nfr / 1E0))
			elif (nfr >= 1E-2):
				print('%.1f cm'%(nfr * 1E2))
			else:
				print('%.1f mm' %(nfr*1E3))
		else:
			print('%.16G' %(nfr))
	elif len(sys.argv)>2 and sys.argv[2] == "nfscount":
		parser = argparse.ArgumentParser(prog="nfscount", description="minimum distance sampling count for near-field antenna measurements", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="explanation:\nfunction returns following outputs respectively:\n  sd: minimum sampling distance\n  ss: sampling start position\n  sf: sampling finish position\n  sc: sampling count\n\n\n\n")
		parser.add_argument("freq", help="frequency of interest in Hertz [Hz]", type=float, nargs=1)
		parser.add_argument("length", help="initial desired sampling length in meters", type=float, nargs=1)
		args = parser.parse_args(sys.argv[3:])
		import math
		import scipy.constants as constants
		nfs = math.floor(0.5*constants.speed_of_light/args.freq[0]*1E3)
		len = math.ceil(args.length[0]*1E3)
		len = len/2 if len%2==0 else (len+1)/2
		if len%nfs > 0:
			len = len + (nfs-len%nfs)
		print('%d %.3f %.3f %d'%(nfs,-float(len)/1000,+float(len)/1000,2*(len/nfs)+1))
	elif len(sys.argv)>2 and sys.argv[2] == "nfsminlen":
		parser = argparse.ArgumentParser(prog="nfsminlen", description="minimum sampling distance for near-field antenna measurements", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n\nformula:\nR_{nf} &= \\lambda/2 = c_0/(2\\timesf)\n\nreferences:\n- IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.2.5, Page 23, Equation 25")
		parser.add_argument("freq", help="frequency of interest in Hertz [Hz]", type=float, nargs=1)
		parser.add_argument("--human", help="human readable output like mm, cm, m", action="store_true")
		args = parser.parse_args(sys.argv[3:])
		import math
		import scipy.constants as constants
		nfs = 0.5*constants.speed_of_light/args.freq[0]
		if args.human: 
			print('%d mm'%(math.floor(nfs*1E3)))
		else:
			print('%.16G' %(nfs))
	elif len(sys.argv)>2 and sys.argv[2] == "snfmre":
		parser = argparse.ArgumentParser(prog="snfmre", description="calculates minimum radius enclosed (MRE) of the antenna for spherical near-field (SNF) measurements", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n\nformula:\nmre &= \\sqrt{dx^2+dy^2+dz^2}\n\n")
		parser.add_argument("dx", help="max displacement from rotation center along x-axis", type=float, nargs=1)
		parser.add_argument("dy", help="max displacement from rotation center along y-axis", type=float, nargs=1)
		parser.add_argument("dz", help="max displacement from rotation center along z-axis", type=float, nargs=1)
		args = parser.parse_args(sys.argv[3:])
		import math
		print('%.16G' %(math.sqrt(args.dx[0]**2+args.dy[0]**2+args.dz[0]**2)))
	else:
		parser = argparse.ArgumentParser(prog="antenna", description="Measurement Module")
		parser.add_argument("nfrange", help="[f] minimum recommended distance for near-field antenna measurements", type=str, nargs="?")
		parser.add_argument("nfscount", help="[f] minimum distance sampling count for near-field antenna measurements", type=str, nargs="?")
		parser.add_argument("nfsminlen", help="[f] minimum sampling distance for near-field antenna measurements", type=str, nargs="?")
		parser.add_argument("snfmre", help="[f] calculates minimum radius enclosed (MRE) of the antenna for spherical near-field (SNF) measurements", type=str, nargs="?")
		print(parser.format_help().replace("positional arguments","module/function").replace("[nfrange] ","").replace("[nfscount] ","").replace("[nfsminlen] ","").replace("[snfmre] ","").replace("[snfmre]","[module/function]"))
elif len(sys.argv)>1 and sys.argv[1] == "propagation":
	if len(sys.argv)>2 and sys.argv[2] == "ffdist":
		parser = argparse.ArgumentParser(prog="ffdist", description="far-field (Fraunhofer) distance of an antenna or aperture", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n\nformula:\nR_{ff} &= Max\\left(\\dfrac{2D^2}{\\lambda},5D,1.6\\lambda\\right)\n\nreferences:\n- Warren L. Stutzman, Antenna Theory and Design, 3rd Ed., Page 43")
		parser.add_argument("D", help="maximum cross-sectional size", type=float, nargs=1)
		parser.add_argument("freq", help="frequency of interest in Hz", type=float, nargs=1)
		parser.add_argument("--human", help="human readable output like cm, mm, km", action="store_true")
		args = parser.parse_args(sys.argv[3:])
		import scipy.constants as constants
		wle = constants.speed_of_light/args.freq[0]
		rff = max(2*args.D[0]**2/wle, 5*args.D[0], 1.5*wle)
		if args.human:
			if (rff >= 1E3):
				print('%.1f km'%(rff / 1E3))
			elif (rff >= 1):
				print('%.1f m'%(rff / 1E0))
			elif (rff >= 1E-2):
				print('%.1f cm'%(rff * 1E2))
			else:
				print('%.1f mm'%(rff*1E3))
		else:
			print('%.16G' %(rff))
	elif len(sys.argv)>2 and sys.argv[2] == "lineofsight":
		parser = argparse.ArgumentParser(prog="lineofsight", description="line-of-sight range in kilometers [km] for a given height", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n\nformula:\nR_{los} &= \\sqrt{2\\cdotR\\cdoth} \\approx 3.57\\times\\sqrt{h} [km]\n\nreferences:\n- https://en.wikipedia.org/wiki/Line-of-sight_propagation")
		parser.add_argument("height", help="height of transmitter/recevier above ground in meters [m]", type=float, nargs="+")
		args = parser.parse_args(sys.argv[3:])
		import numpy
		rhz = 3.57*numpy.sqrt(args.height)
		numpy.set_printoptions(precision=3)
		numpy.savetxt(sys.stdout,rhz,fmt='%.16G')
	elif len(sys.argv)>2 and sys.argv[2] == "pathloss":
		parser = argparse.ArgumentParser(prog="pathloss", description="free space path loss", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n\nformula:\nL_P &= 32.45 + 20\\log10(fR) - G_1 - G_2 \\quad [dB]\n\nreferences:\n- Thomas A. Milligan, Modern Antenna Design, 2nd Ed., Chapter 3, Page 6")
		parser.add_argument("freq", help="frequency of interest in MegaHertz [MHz]", type=float, nargs=1)
		parser.add_argument("R", help="range in kilometers [m]", type=float, nargs=1)
		parser.add_argument("--g1", help="gain of transmitter antenna in [dB]", default="0", type=float, nargs=1)
		parser.add_argument("--g2", help="gain of receiver antenna in [dB]", default="0", type=float, nargs=1)
		args = parser.parse_args(sys.argv[3:])
		import math
		pls = 32.45 + 20*math.log10(args.freq[0]*args.R[0]) - args.g1 - args.g2
		print('%.16G' %(pls))
	elif len(sys.argv)>2 and sys.argv[2] == "radiohorizon":
		parser = argparse.ArgumentParser(prog="radiohorizon", description="radio horizon in kilometers [km] for a given height", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="\n\nformula:\nR_{rad} &\\approx 4.12\\times\\sqrt{h} [km]\n\nreferences:\n- https://en.wikipedia.org/wiki/Line-of-sight_propagation")
		parser.add_argument("height", help="height of transmitter/recevier above ground in meters [m]", type=float, nargs="+")
		args = parser.parse_args(sys.argv[3:])
		import numpy
		rhz = 4.12*numpy.sqrt(args.height)
		numpy.set_printoptions(precision=3)
		numpy.savetxt(sys.stdout,rhz,fmt='%.16G')
	else:
		parser = argparse.ArgumentParser(prog="antenna", description="Propagation Module")
		parser.add_argument("ffdist", help="[f] far-field (Fraunhofer) distance of an antenna or aperture", type=str, nargs="?")
		parser.add_argument("lineofsight", help="[f] line-of-sight range in kilometers [km] for a given height", type=str, nargs="?")
		parser.add_argument("pathloss", help="[f] free space path loss", type=str, nargs="?")
		parser.add_argument("radiohorizon", help="[f] radio horizon in kilometers [km] for a given height", type=str, nargs="?")
		print(parser.format_help().replace("positional arguments","module/function").replace("[ffdist] ","").replace("[lineofsight] ","").replace("[pathloss] ","").replace("[radiohorizon] ","").replace("[radiohorizon]","[module/function]"))
else:
	parser = argparse.ArgumentParser(prog="antenna", description="Antenna Toolkit")
	parser.add_argument("freq2wlen", help="[f] frequency to wavelength conversion", type=str, nargs="?")
	parser.add_argument("gamma2swr", help="[f] reflection coefficient (gamma) to standing wave ratio (swr) conversion", type=str, nargs="?")
	parser.add_argument("swr2gamma", help="[f] standing wave ratio (swr) to reflection coefficient (gamma) conversion", type=str, nargs="?")
	parser.add_argument("wlen2freq", help="[f] wavelength to frequency conversion", type=str, nargs="?")
	parser.add_argument("measurement", help="[m] Measurement Module", type=str, nargs="?")
	parser.add_argument("propagation", help="[m] Propagation Module", type=str, nargs="?")
	print(parser.format_help().replace("positional arguments","module/function").replace("[freq2wlen] ","").replace("[gamma2swr] ","").replace("[swr2gamma] ","").replace("[wlen2freq] ","").replace("[measurement] ","").replace("[propagation] ","").replace("[propagation]","[module/function]"))
