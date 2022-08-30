import subprocess
from benchtograph import *


def format_verilog(netlist,remove_wire=False) -> str:
  netlist = re.sub(r"\\", "", netlist)
  netlist=re.sub("[/][*].*[*][/]","",netlist)
  netlist=re.sub("[(][*].*[*][)]\n","",netlist)
  if(remove_wire):
    netlist=re.sub(" ?wire .*;\n","",netlist)
  
  # netlist=re.sub("assign .* = .*;","",netlist) #replace with rmassign fn

  netlist=re.sub("\n+","",netlist)
  netlist=re.sub("\s+"," ",netlist)
  netlist=re.sub("(\s+;)|(;)"," ;\n",netlist)
  netlist = re.sub(r"//.*\n", "", netlist)
  # netlist=re.sub("endmodule","endmodule\n",netlist)
  return netlist

def extract_io(netlist,mode="input"):
  for i in re.findall(mode+" .*;\n",netlist):
    if("[" in i):
      tmpstr=""
      tmp=re.findall(mode+" \[(\d+):(\d+)\] (.*);",i)[0]
      for k in range(int(tmp[1]),int(tmp[0])+1):
        tmpstr=tmpstr+mode.upper()+"("+tmp[2]+"["+str(k)+"]);"+"\n"
    else:
      tmp=i.split(" ")[-1][:-2]
      tmpstr=mode.upper()+"("+tmp+");"
    
    tmpi=re.sub("\[","\[",i)
    tmpi=re.sub("\]","\]",tmpi)
    netlist=re.sub(tmpi,tmpstr,netlist)
  # netlist=re.sub(r" \[",r"[",netlist)
  return netlist



subprocess.run(cmd1.format("/home/alira/FYP/linux/tmp.v", "/home/alira/FYP/linux/tmpoutput.v",
               "/home/alira/FYP/linux/output.v", getcpp="#", gettmpv=""), shell=True)
netlist = open("/home/alira/FYP/linux/output.v").read()

netlist=format_verilog(netlist,remove_wire=True)
# netlist=extract_io(netlist,mode= "input")
# netlist=extract_io(netlist,mode="output")

assign=re.findall(r"(assign ([a-zA-Z0-9.\[:\]\{\},_\s]*) = ([a-zA-Z0-9.\[:\]\{\},_\s]*) ;)",netlist)
print(len(assign))
for i in assign:
  re.sub(assign[0][0],"",netlist)
  re.sub(assign[0][1],assign[0][2],netlist)


with open("/home/alira/FYP/linux/output.v", 'w') as f:
    f.write(netlist)

# netlist = re.sub("\n", "", netlist)
# netlist = re.sub("\s+", " ", netlist)
# netlist = re.sub(";", ";\n", netlist)

# netlist = re.sub("module\s?(.*)\s?\(\s?", r"\nmodule \1(", netlist)

# netlist = re.sub("[/][*].*[*][/]", "", netlist)
# netlist = re.sub(r"//.*\n", "", netlist)
# netlist = re.sub(r"\\", "", netlist)
# netlist = re.sub(r" \[", "[", netlist)



####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################


# import re
# netlist=open("/home/alira/FYP/python/circuit.v").read()
# tmp=re.findall("key_[0-9]+_",netlist)
# count=0
# for i in range(0,133):
#     if (re.findall("key_"+str(i)+"_",netlist)==[]):
#         print(i,count)
#         pass
#     else:
#         #print(re.findall("key_"+str(i)+"_",netlist))
#         netlist=re.sub("key_"+str(i)+"_","keyinputG"+str(count+1),netlist)
#         #netlist=re.sub("key_"+str(i)+"_","key_"+str(count)+"_",netlist)
#         count+=1
#         print(count)

# with open("./python/tmpcir.bench", 'w') as f:
#     f.write(netlist)







