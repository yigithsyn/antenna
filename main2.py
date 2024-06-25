# import json
import os

name        = ""
description = ""
epilogue    = ""
formula     = []
references  = []
modules     = []

positional_args = []
optional_args   = []
flags           = []
for file in filter(lambda item: os.path.isfile('cmds2/'+item), os.listdir("cmds2")):
  with open("cmds2/%s"%(file), "r") as file:
    # print(file.read())
    file_data = file.read()
    exec(file_data)
    # print(name)
    # print(description)
    # print(epilogue)
    # print(modules)
    # print(positional_args)
    # print(optional_args)
    # print(flags)
    # print("\n\n")
    with open("%s.py"%name, "w") as file:
      file.write("import sys\n")
      file.write("import argparse\n")
      file.write("\n")
      file.write(file_data.split("name")[0])

      file.write('parser = argparse.ArgumentParser(prog="%s", description="%s", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="%s%s\\n\\n%s%s")\n'%(name,description,'formula:\\n' if formula else '','\\n'.join(formula).replace('\\','\\\\'),'references:\\n- ' if references else '','\\n- '.join(references)))
      for item in positional_args:
        arg_count = '"%s"'%item['count'] if type(item['count']) == str else '%d'%item['count'] 
        file.write('parser.add_argument("%s", help="%s", type=%s, nargs=%s)\n'%(item['name'], item['description'], item['type'], arg_count))
      for item in optional_args:
        arg_count = '"%s"'%item['count'] if type(item['count']) == str else '%d'%item['count'] 
        file.write('parser.add_argument("--%s", help="%s", default="%s", type=%s, nargs=%s)\n'%(item['name'], item['description'], str(item['default']), item['type'], arg_count))
      for item in flags:
        file.write('parser.add_argument("--%s", help="%s", action="store_true")\n'%(item['name'], item['description']))
      file.write('args = parser.parse_args(sys.argv[1:])')
      file.write("\n")

      file.write(file_data.split("args = {}")[1])
      # file.write("print(wavelength)")

# cmds = []
# for file in filter(lambda itm: os.path.isfile('cmds/'+itm), os.listdir("cmds")):
#     with open('cmds/'+file) as file:
#         cmds.append(json.loads(file.read()))
# for fold in filter(lambda itm: os.path.isdir('cmds/'+itm), os.listdir("cmds")):
#     with open('cmds/'+fold+'/index.json') as file:
#         cmds.append(json.loads(file.read()))
#         cmds[-1]['cmds'] = []
#     for file in filter(lambda itm: os.path.isfile('cmds/'+fold+'/'+itm) and itm!='index.json', os.listdir('cmds/'+fold)):
#         with open('cmds/'+fold+'/'+file) as file:
#               cmds[-1]['cmds'].append(json.loads(file.read()))
# with open('main.json', 'w') as file:
#     json.dump(cmds, file, indent=4)

# print("import sys")
# print("import argparse")
# print(" ")

# i = 0
# for cmd in filter(lambda itm: ("cmds" not in itm), cmds):
#     print('%s len(sys.argv)>1 and sys.argv[1] == "%s":'%("if" if i==0 else "elif", cmd['name']))
#     print('\tparser = argparse.ArgumentParser(prog="%s", description="%s", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="%s%s\\n\\n%s%s")'%(cmd['name'],cmd['desc'],'formula:\\n' if cmd['frml'] else '','\\n'.join(cmd['frml']).replace('\\','\\\\'),'references:\\n- ' if cmd['rfrs'] else '','\\n- '.join(cmd['rfrs'])))
#     for prg in cmd['prgs']:
#         nrg = '"%s"'%prg['cunt'] if type(prg['cunt']) == str else '%d'%prg['cunt'] 
#         print('\tparser.add_argument("%s", help="%s", type=%s, nargs=%s)'%(prg['name'], prg['desc'], prg['type'], nrg))
#     for org in cmd['orgs']:
#             nrg = '"%s"'%org['cunt'] if type(org['cunt']) == str else '%d'%org['cunt'] 
#             print('\t\tparser.add_argument("--%s", help="%s", default="%s", type=%s, nargs=%s)'%(org['name'], org['desc'], str(org['dflt']), org['type'], nrg))
#     for flg in cmd['flgs']:
#         print('\tparser.add_argument("--%s", help="%s", action="store_true")'%(flg['name'], flg['desc']))
#     print('\targs = parser.parse_args(sys.argv[2:])')
#     for req in cmd['reqs']:
#         print('\timport %s'%req)
#     for syn in cmd['code']:
#         print('\t%s'%syn)
#     i = i+1

# for cmd in filter(lambda itm: ("cmds" in itm), cmds):
#     print('%s len(sys.argv)>1 and sys.argv[1] == "%s":'%("if" if i==0 else "elif", cmd['name']))
#     desc = cmd['desc']
#     cmds = cmd['cmds']
#     i = 0
#     for cmd in cmds:
#         print('\t%s len(sys.argv)>2 and sys.argv[2] == "%s":'%("if" if i==0 else "elif", cmd['name']))
#         print('\t\tparser = argparse.ArgumentParser(prog="%s", description="%s", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="%s%s\\n\\n%s%s\\n\\n%s%s")'%(cmd['name'],cmd['desc'],'explanation:\\n' if cmd['eplg'] else '','\\n'.join(cmd['eplg']),'formula:\\n' if cmd['frml'] else '','\\n'.join(cmd['frml']),'references:\\n- ' if cmd['rfrs'] else '','\\n- '.join(cmd['rfrs'])))
#         for prg in cmd['prgs']:
#             nrg = '"%s"'%prg['cunt'] if type(prg['cunt']) == str else '%d'%prg['cunt'] 
#             print('\t\tparser.add_argument("%s", help="%s", type=%s, nargs=%s)'%(prg['name'], prg['desc'], prg['type'], nrg))
#         for org in cmd['orgs']:
#             nrg = '"%s"'%org['cunt'] if type(org['cunt']) == str else '%d'%org['cunt'] 
#             print('\t\tparser.add_argument("--%s", help="%s", default="%s", type=%s, nargs=%s)'%(org['name'], org['desc'], str(org['dflt']), org['type'], nrg))
#         for flg in cmd['flgs']:
#             print('\t\tparser.add_argument("--%s", help="%s", action="store_true")'%(flg['name'], flg['desc']))
#         print('\t\targs = parser.parse_args(sys.argv[3:])')
#         for req in cmd['reqs']:
#             print('\t\timport %s'%req)
#         for syn in cmd['code']:
#             print('\t\t%s'%syn)
#         i = i+1
#     print('\telse:')
#     print('\t\tparser = argparse.ArgumentParser(prog="antenna", description="%s")'%desc)
#     for cmd in filter(lambda itm: ("cmds" not in itm), cmds):
#         print('\t\tparser.add_argument("%s", help="[f] %s", type=str, nargs="?")'%(cmd['name'], cmd['desc']))
#     for cmd in filter(lambda itm: ("cmds" in itm), cmds):
#         print('\t\tparser.add_argument("%s", help="[m] %s", type=str, nargs="?")'%(cmd['name'], cmd['desc']))
#     print('\t\tprint(parser.format_help().replace("positional arguments","module/function")', end='')
#     for cmd in cmds:
#         print('.replace("[%s] ","")'%cmd['name'], end="")
#     print('.replace("[%s]","[module/function]"))'%cmds[-1]['name'])

# with open('main.json') as file:
#     cmds = json.loads(file.read())
# print('else:')
# print('\tparser = argparse.ArgumentParser(prog="antenna", description="Antenna Toolkit")')
# for cmd in filter(lambda itm: ("cmds" not in itm), cmds):
#     print('\tparser.add_argument("%s", help="[f] %s", type=str, nargs="?")'%(cmd['name'], cmd['desc']))
# for cmd in filter(lambda itm: ("cmds" in itm), cmds):
#     print('\tparser.add_argument("%s", help="[m] %s", type=str, nargs="?")'%(cmd['name'], cmd['desc']))
# print('\tprint(parser.format_help().replace("positional arguments","module/function")', end='')
# for cmd in cmds:
#     print('.replace("[%s] ","")'%cmd['name'], end="")
# print('.replace("[%s]","[module/function]"))'%cmds[-1]['name'])

# os.remove("main.json")