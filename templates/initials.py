snme = ""                                             
lnme = ""                                          
desc = ""                                  
fncs = []
expl = []                                                 
frml = []                                                 
auth = []
refs = []                                                 
parg = []                                                 
oarg = []                                                 
flag = []      

# preparation for parsing 
flst = []                                                 
for i in range(len(fncs)):
  flst.append("  %s: %s"%(fncs[i]["snme"].ljust(4),fncs[i]["desc"]))
for i in range(len(frml)):
  frml[i] = "  " + frml[i]
for i in range(len(expl)):
  expl[i] = "  " + expl[i]
for i in range(len(auth)):
  auth[i] = "  " + auth[i]
for i in range(len(refs)):
  refs[i] = "  - " + refs[i]
