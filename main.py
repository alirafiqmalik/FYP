import src.LL as L
import src.utils as u
import src.conv as c
from src.cmds import *
import subprocess





b=open("/home/alira/FYP/linux/MSATLL/benchmarks/original/apex4.bench").read()
tmp=L.LogicLocking(b)
tmp.SLL(10,75)
# tmp.SFLLHD(outputpath="/home/alira/FYP/tmp/tmpsll.bench", HD=0, key=734)
tmp.graph_to_bench("/home/alira/FYP/tmp/tmp_sll.bench")

bl=open("/home/alira/FYP/tmp/tmp_sll.bench").read()

to,_=c.bench_to_verilog(b)
with open("/home/alira/FYP/tmp/tmp_org.v",'w') as f:
  f.write(to)

t1,_=c.bench_to_verilog(bl)
with open("/home/alira/FYP/tmp/tmp_sll.v",'w') as f:
  f.write(t1)





# subprocess.run(cmd2.format("/home/alira/FYP/tmp/tmp_sll.bench",
#                        "/home/alira/FYP/tmp/tmp_sll.v"), shell=True)

# subprocess.run(cmd2.format("/home/alira/FYP/linux/MSATLL/benchmarks/original/apex4.bench",
#                        "/home/alira/FYP/tmp/tmp_org.v"), shell=True)















# verilog=open("/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/tmpout.v").read()

# inputs=u.getio_v(verilog,"input")
# outputs=u.getio_v(verilog,"output")
# gates,_=u.extract_gates_v(verilog)


# bench=open("/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/oracle1.bench").read()
# tmp,_=c.bench_to_verilog(bench)

# # print(tmp)
# with open("./tmp/tmpbench_to_v_oracle1.v",'w') as f:
#   f.write(tmp)



# bench=open("/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1.bench").read()
# tmp,_=c.bench_to_verilog(bench)
# with open("./tmp/tmpbench_to_v_design1.v",'w') as f:
#   f.write(tmp)




































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