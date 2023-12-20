import subprocess
from src.netlist import Netlist

yosys_path="/home/alira/FYP/linux/yosys/build/yosys"
abc_path="/home/alira/FYP/linux/yosys/build/yosys-abc"



# /home/alira/FYP/linux/yosys/build/yosys -p '
# read_verilog tmp.v
# hierarchy -check -top top
# flatten
# proc; opt; fsm; opt; memory; opt
# techmap; opt
# dfflibmap -liberty /home/alira/FYP/linux/mycells.lib
# # abc -liberty /home/alira/FYP/linux/mycells.lib
# write_verilog -noattr tmprtl.v
# '

# /home/alira/FYP/tmp2.v
# /home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1_netlist.v

# /home/alira/FYP/linux/yosys/build/yosys -p '
# read_verilog /home/alira/FYP/linux/CSAW/modulefiles.v /home/alira/FYP/tmp2.v
# hierarchy -check -top pancham
# flatten
# proc; opt; fsm; opt; memory; opt
# techmap; opt
# dfflibmap -liberty /home/alira/FYP/vlib/mycells.lib
# abc -liberty /home/alira/FYP/vlib/mycells.lib
# write_verilog -noattr tmpout.v
# '




# /home/alira/FYP/linux/yosys/build/yosys -p '
# read_verilog /home/alira/FYP/linux/CSAW/modulefiles.v /home/alira/FYP/tmp2.v
# hierarchy -check -top pancham
# flatten
# proc; opt; fsm; opt; memory; opt
# techmap; opt
# write_verilog -noattr tmpout.v
# '



cmd1=yosys_path+""" -p '
read_verilog {inputfile}
hierarchy -check -top top
flatten
{getcpp}write_cxxrtl {cppfile}
proc; opt; fsm; opt; memory; opt
techmap; opt
{gettmpv}write_verilog -noattr {rtlv}
dfflibmap -liberty /home/alira/FYP/vlib/mycells.lib
abc -liberty /home/alira/FYP/vlib/mycells.lib

write_verilog -noattr {outputfile}
'
"""

cmd2=abc_path+r" -c 'read_bench {};write_verilog {}'"
#
# """
# # cwd=$(pwd)
# # #echo $cwd
# """+abc_path+"\n"+abc_path+"""/yosys-abc -c 'read_bench {};write_verilog {}'
# # cd $cwd
# """


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


# subprocess.run(cmd2.format("/home/alira/FYP/tmp/tmp_sll.bench",
#                        "/home/alira/FYP/tmp/tmp_sll.v"), shell=True)

# subprocess.run(cmd2.format("/home/alira/FYP/linux/MSATLL/benchmarks/original/apex4.bench",
#                        "/home/alira/FYP/tmp/tmp_org.v"), shell=True)



# python3 /home/alira/FYP/sat_attack/run.py /home/alira/FYP/tmp.bench /home/alira/FYP/tmp2.bench b
# python3 /home/alira/FYP/sat_attack/run.py /home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1.bench /home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/oracle1.bench b


# ./sld /home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1.bench /home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/oracle1.bench

# /home/alira/FYP/linux/yosys/build/yosys -p '
# read_verilog /home/alira/FYP/linux/CSAW/modulefiles.v /home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1_netlist.v
# hierarchy -check -top fsm_0_obf
# flatten
# proc; opt; fsm; opt; memory; opt
# techmap; opt
# dfflibmap -liberty /home/alira/FYP/vlib/mycells.lib
# abc -liberty /home/alira/FYP/vlib/mycells.lib
# write_verilog -noattr tmpout.v
# '


# /home/alira/FYP/linux/yosys/build/yosys -p '
# read_verilog /home/alira/FYP/linux/vga_demo.v
# hierarchy -check -top vga_demo
# flatten
# proc; opt; fsm; opt; memory; opt
# techmap; opt
# dfflibmap -liberty /home/alira/FYP/vlib/mycells.lib
# abc -liberty /home/alira/FYP/vlib/mycells.lib
# write_verilog -noattr /home/alira/FYP/linux/assign_tech.v
# '

# """
# /home/alira/FYP/linux/yosys/build/yosys -p
# read_verilog tmptop.v 
# hierarchy -check -top top
# flatten
# proc; opt; fsm; opt; memory; opt
# techmap; opt
# dfflibmap -liberty /home/alira/FYP/vlib/mycells.lib
# abc -liberty /home/alira/FYP/vlib/mycells.lib
# write_verilog -noattr tmp.v
# """


# "/home/alira/FYP/linux/yosys/build/yosys -p 'read_verilog tmptop.v ;hierarchy -check -top top;flatten ;proc; opt; fsm; opt; memory; opt;dfflibmap -liberty /home/alira/FYP/vlib/mycells.lib;abc -liberty /home/alira/FYP/vlib/mycells.lib;write_verilog -noattr tmp.v'"



# subprocess.run(cmds,shell=True)



