import re
import subprocess
from benchtograph import *


cmd4="""
cwd=$(pwd)
#echo $cwd
cd /home/alira/FYP/linux/yosys/build
./yosys-abc -c 'read_bench /home/alira/FYP/org.bench;write_verilog /home/alira/FYP/btv_org.v'
cd $cwd
"""

cmd5="""
/home/alira/FYP/linux/yosys/build/yosys -p '
read_verilog /home/alira/FYP/linux/tmp.v
hierarchy -check -top top
flatten
proc; opt; fsm; opt; memory; opt
techmap; opt
dfflibmap -liberty /home/alira/FYP/linux/mycells.lib
#abc -genlib libfile.genlib
abc -liberty /home/alira/FYP/linux/mycells.lib
clean
write_verilog -noexpr /home/alira/FYP/btv_org_yosys.v
'
"""


# netlist=open("/home/alira/FYP/netlist.bench").read()

# subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/linux/final.v",shell=True)
# netlist=open("/home/alira/FYP/linux/final.v").read()
# org=Netlist(netlist)

# org.graph_to_bench("/home/alira/FYP/org.bench")
# subprocess.run(cmd4,shell=True)
# subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/btv_org.v \/home/alira/FYP/org",shell=True)


# subprocess.run(cmd5,shell=True)
# subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/btv_org_yosys.v ",shell=True)


