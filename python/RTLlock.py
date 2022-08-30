from benchtograph import *
import subprocess
import re


cmd1="""
yosys -p '
read_verilog  top.v
proc
techmap; opt
write_verilog -noattr ./tmpoutput.v'
"""


cmd2="""
yosys -p '
read_verilog rtloutput.v
hierarchy -check -top top
flatten
proc; opt; fsm; opt; memory; opt
techmap; opt
write_verilog -noattr ./abc_rtloutput.v
dfflibmap -liberty yosys/manual/PRESENTATION_Intro/mycells.lib
abc -liberty yosys/manual/PRESENTATION_Intro/mycells.lib
clean
write_verilog -noattr ./yosys_rtloutput.v
'
"""

# tmpval,tmpkey=randKey()

subprocess.run("clear",shell=True)
subprocess.run(cmd1,shell=True)

netlist=open('/home/alira/FYP/tmpoutput.v').read()

# keytable={}
# for i,x in enumerate(re.findall("assign .* [0-9]*'h[0-9abcdef]*.*",netlist)):
  
#   if(re.findall("[0-9]*'h[0-9abcdef]*",x)[0] in keytable.keys()):
#     keytable[re.findall("[0-9]*'h[0-9abcdef]*",x)[0]].append("key_"+str(i))
#   else:
#     keytable[re.findall("[0-9]*'h[0-9abcdef]*",x)[0]]=["key_"+str(i)]

# for i,x in enumerate(keytable.keys()):
#   bit_width,hexval=x.split("'h")
#   if(bit_width=="16" or bit_width=="8"):
#     val=int(hexval,16)
#     print(i,x)
#     netlist=re.sub("key_"+str(i),x,netlist)


# netlist=re.sub("key_0",r"8'h00",netlist)
# netlist=re.sub("key_1","16'h0000",netlist)

print(re.findall("8'h00",netlist))

netlist=re.sub("8'h00","key[7:0]",netlist)
netlist=re.sub("16'h0000","key[23:8]",netlist)

netlist=re.sub("(module top\(.*)(\);)",r"\1"+",key);"+"\ninput [23:0]key;wire [23:0]key;",netlist)




print(re.findall("8'h00",netlist))

with open("/home/alira/FYP/rtloutput.v", 'w') as f:
    f.write(netlist)



subprocess.run(cmd2,shell=True)
subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/yosys_rtloutput.v",shell=True)