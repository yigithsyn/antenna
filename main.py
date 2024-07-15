# import json
import os
from pathlib import Path

snme = ""
lnme = ""
desc = ""
eplg = []
frml = []
refs = []
modl = []

parg = []
oarg = []
flag = []

flds = {
  "util": {"lnme": "utility", "desc": "Utility functions"}
}

Path.mkdir("./scripts/util", parents=True)

for fold in filter(lambda item: os.path.isdir('cmds/'+item), os.listdir("cmds2")):
  # 4 letter version
  with open("./scripts/4letter/ante.%s.py"%(fold), "w") as file:
    file.write("from sys import argv\n")
    file.write("from argparse import ArgumentParser, RawDescriptionHelpFormatter\n")
    file.write("\n")
    fncs = []
    for item in filter(lambda item: os.path.isfile('cmds/'+fold+"/"+item), os.listdir('cmds/'+fold)):
      with open("cmds/%s/%s"%(fold, item), "r") as fl2e:
        file_data = fl2e.read()
        exec(file_data)
        fncs.append("  %s: %s"%(snme.ljust(4), desc))
    file.write('pars = ArgumentParser(prog="ante.%s", description="%s", formatter_class=RawDescriptionHelpFormatter, epilog="%s%s")\n'%(fold,flds[fold]["desc"],'functions:\\n' if fncs else '','\\n'.join(fncs)))
    file.write('args = pars.parse_args(["--help"])')
  # canonic version
  with open("./scripts/canonic/antenna.%s.py"%(flds[fold]["lnme"]), "w") as file:
    file.write("from sys import argv\n")
    file.write("from argparse import ArgumentParser, RawDescriptionHelpFormatter\n")
    file.write("\n")
    fncs = []
    for item in filter(lambda item: os.path.isfile('cmds/'+fold+"/"+item), os.listdir('cmds/'+fold)):
      with open("cmds/%s/%s"%(fold, item), "r") as fl2e:
        file_data = fl2e.read()
        exec(file_data)
        fncs.append("  %s: %s"%(lnme.ljust(4), desc))
    file.write('pars = ArgumentParser(prog="antenna.%s", description="%s", formatter_class=RawDescriptionHelpFormatter, epilog="%s%s")\n'%(flds[fold]["lnme"],flds[fold]["desc"],'functions:\\n' if fncs else '','\\n'.join(fncs)))
    file.write('args = pars.parse_args(["--help"])')
  

  for file in filter(lambda item: os.path.isfile('cmds/'+fold+"/"+item), os.listdir('cmds/'+fold)):
    with open("cmds/%s/%s"%(fold, file), "r") as file:
      file_data = file.read()
      exec(file_data)
      # 4 letter version
      with open("./scripts/4letter/ante.%s.%s.py"%(fold,snme), "w") as file:
        file.write("from sys import argv\n")
        file.write("from argparse import ArgumentParser, RawDescriptionHelpFormatter\n")
        file.write("\n")
        file.write(file_data.split("snme")[0])
        file.write('pars = ArgumentParser(prog="ante.%s.%s", description="%s", formatter_class=RawDescriptionHelpFormatter, epilog="%s%s\\n\\n%s%s\\n\\n%s%s")\n'%(fold,snme,desc,'explanation:\\n' if eplg else '','\\n'.join(eplg), 'formula:\\n' if frml else '','\\n'.join(frml).replace('\\','\\\\'),'references:\\n- ' if refs else '','\\n- '.join(refs)))
        for item in parg:
          cont = '"%s"'%item['cont'] if type(item['cont']) == str else '%d'%item['cont']
          file.write('pars.add_argument("%s", help="%s", type=%s, nargs=%s)\n'%(item['name'], item['desc'], item['type'], cont))
        for item in oarg:
          cont = '"%s"'%item['cont'] if type(item['cont']) == str else '%d'%item['cont'] 
          file.write('pars.add_argument("--%s", help="%s", default="%s", type=%s, nargs=%s)\n'%(item['name'], item['desc'], str(item['default']), item['type'], cont))
        for item in flag:
          file.write('pars.add_argument("--%s", help="%s", action="store_true")\n'%(item['name'], item['desc']))
        file.write('args = pars.parse_args(argv[1:])')
        file.write("\n")
        file.write(file_data.split("# implementation")[1])
      # canonic version
      with open("./scripts/canonic/antenna.%s.%s.py"%(flds[fold]["lnme"],lnme), "w") as file:
        file.write("import sys\n")
        file.write("import argparse\n")
        file.write("\n")
        file.write(file_data.split("snme")[0])
        file.write('pars = argparse.ArgumentParser(prog="antenna.%s.%s", description="%s", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="%s%s\\n\\n%s%s\\n\\n%s%s")\n'%(flds[fold],lnme,desc,'explanation:\\n' if eplg else '','\\n'.join(eplg), 'formula:\\n' if frml else '','\\n'.join(frml).replace('\\','\\\\'),'references:\\n- ' if refs else '','\\n- '.join(refs)))
        for item in parg:
          cont = '"%s"'%item['cont'] if type(item['cont']) == str else '%d'%item['cont']
          file.write('pars.add_argument("%s", help="%s", type=%s, nargs=%s)\n'%(item['name'], item['desc'], item['type'], cont))
        for item in oarg:
          cont = '"%s"'%item['cont'] if type(item['cont']) == str else '%d'%item['cont'] 
          file.write('pars.add_argument("--%s", help="%s", default="%s", type=%s, nargs=%s)\n'%(item['name'], item['desc'], str(item['default']), item['type'], cont))
        for item in flag:
          file.write('pars.add_argument("--%s", help="%s", action="store_true")\n'%(item['name'], item['desc']))
        file.write('args = pars.parse_args(sys.argv[1:])')
        file.write("\n")
        file.write(file_data.split("# implementation")[1])
