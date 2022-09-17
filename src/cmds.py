import subprocess
from netlist import Netlist

yosys_path="/home/alira/FYP/linux/yosys/build/yosys"
abc_path="/home/alira/FYP/linux/yosys/build"



/home/alira/FYP/linux/yosys/build/yosys -p '
read_verilog tmp.v
hierarchy -check -top top
flatten
proc; opt; fsm; opt; memory; opt
techmap; opt
dfflibmap -liberty /home/alira/FYP/linux/mycells.lib
# abc -liberty /home/alira/FYP/linux/mycells.lib
write_verilog -noattr tmprtl.v
'


cmd1=yosys_path+""" -p '
read_verilog {inputfile}
hierarchy -check -top top
flatten
{getcpp}write_cxxrtl {cppfile}
proc; opt; fsm; opt; memory; opt
techmap; opt
{gettmpv}write_verilog -noattr {rtlv}
dfflibmap -liberty /home/alira/FYP/linux/mycells.lib
abc -liberty /home/alira/FYP/linux/mycells.lib

write_verilog -noattr {outputfile}
'
"""

cmd2="""
cwd=$(pwd)
#echo $cwd
cd """+abc_path+"\n"+abc_path+"""/yosys-abc -c 'read_bench {};write_verilog {}'
cd $cwd
"""


####################################################################################################################
####################################################################################################################
def yosys_cmd():    
    pass


####################################################################################################################
####################################################################################################################
def abc_cmd():    
    pass


####################################################################################################################
####################################################################################################################
def readtopv():
    netlist=open("/home/alira/FYP/top.v").read()
    with open("./tmp/input.v", 'w') as f:
        f.write(netlist)
    subprocess.run(cmd1.format("input.v","./tmpoutput.v","./output.v",getcpp="",gettmpv=""),shell=True)
    subprocess.run("python3 /home/alira/FYP/python/misc_vtb_obs.py",shell=True)
    netlist=open("/home/alira/FYP/netlist.bench").read()
    return netlist
####################################################################################################################
####################################################################################################################
def readbench():
    netlist=open("/home/alira/FYP/input.bench").read()
    org=Netlist(netlist)
    org.graph_to_bench("./org.bench")
    subprocess.run(cmd2.format("/home/alira/FYP/org.bench","/home/alira/FYP/btv_org.v"),shell=True)
    subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/btv_org.v \/home/alira/FYP/org",shell=True)
    subprocess.run(cmd1.format("/home/alira/FYP/btv_org.v","","/home/alira/FYP/btv_org_yosys.v",getcpp="#",gettmpv="#"),shell=True)
    subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/btv_org_yosys.v ",shell=True)
    del org
    return netlist