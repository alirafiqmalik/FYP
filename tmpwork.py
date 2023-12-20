import src.verification as verification
import src.utils as utils
import src.conv as conv
import networkx as nx
import src.LL as LL
import subprocess
import os
import re

cmds="""
./linux/yosys/build/yosys -q -p'
read_verilog {} 
hierarchy -check -top {}
proc; opt; fsm; opt; memory; opt;
techmap; opt
flatten
dfflibmap -liberty ./vlib/mycells.lib
abc -liberty ./vlib/mycells.lib
clean
write_verilog -noattr {}
'
"""



orgdir="./Benchmarks/ISCAS85/"
for files in os.listdir(orgdir):
  orgpath=orgdir+"{orgname}/{orgname}.v".format(orgname=files)
  # print(orgpath,files)

  file_path="./tmpveriog.v"
  netlist=open(file_path).read()
  # print(netlist)

  subprocess.run(cmds.format(file_path,re.findall("module (.*)\(",netlist)[0],"./tmp2.v"),shell=True)

  print("READING DONE")


  verilog=open("./tmp2.v").read()
  verilog=utils.format_verilog(verilog,remove_wire=True)

  with open("./tmp2.v", 'w') as f:
      f.write(verilog)

  # assign_nodes=re.findall("assign (\\?.*) = (.*) ?;\n",verilog)
  # verilog=re.sub("assign (.*) = (.*) ?;\n","",verilog) #BUF_g _node_\1_ ( .A(\2), .Y(\1) );\n
  # print(assign_nodes)
  # for i in assign_nodes:
  #   if(re.findall(i[0],verilog)!=[]):
  #     print(i,re.findall(i[0],verilog))
  #   else:
  #     print(i,re.findall(i[0],verilog))

  # with open("./tmp2.v", 'w') as f:
  #   f.write(verilog)


  # verilog=re.sub("assign (.*) = (.*) ?;\n",r"BUF_g _node_\1_ ( .A(\2), .Y(\1) );\n",verilog)
  
  
  # bench=conv.verilog_to_bench(verilog)

  # # with open("./tmp2.v", 'w') as f:
  # #   f.write(bench)

  # # with open("./tmp2.v","w") as f:
  # #   f.write(verilog)

  # tmpLL=LL.LogicLocking(bench)

  # # tmpLL.nodeio("j")
  
  # # tmpLL.nodeio("NAND_1")
  



  break

  # intkey, tmpkey=utils.randKey(128)
  # tmpLL.RLL(128,intkey)

  # netlistLL=tmpLL.graph_to_bench()

  # outpath="./tmp2LL.bench"
  # print("Writing BENCH File to Location: ", outpath)
  # with open(outpath, 'w') as f:
  #     f.write(netlistLL)
  
  # verilogLL,_=conv.bench_to_verilog(netlistLL,modulename="enccir")
  
  
  
  
  # outpath="./tmp2LL.v"
  # print("Writing BENCH File to Location: ", outpath)
  # with open(outpath, 'w') as f:
  #     f.write(verilogLL)

  


  
  # miter_circuit,miter_testbench=verification.gen_miterCircuit(verilog,verilogLL)

  # with open("top.v","w") as f:
  #   f.write(miter_circuit)
  # with open("testbench.v","w") as f:
  #   f.write(miter_testbench)

  
  # # subprocess.run(cmds.format("tmpveriog.v",re.findall("module (.*)\(",netlist)[0],"./tmpxx.v"),shell=True)
  # # verilog=open("./tmpxx.v").read()
  # # verilog=utils.format_verilog(verilog,remove_wire=True)

  # # with open("/home/alira/FYP/tmpxx.v", 'w') as f:
  # #     f.write(verilog)
  
  # break


#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################




# LL.LogicLocking()





# print(utils.gencc_AntiSAT("top", ["a","b","c"]))

# tmp1=open("./linux/neos/bench/tmpout.bench").read()
# tmp1,_=conv.bench_to_verilog(tmp1)

# tmp2=open("./linux/neos/bench/tmpin.bench").read()
# tmp2,_=conv.bench_to_verilog(tmp2)

# with open("./tmp.v","w") as f:
#   f.write(tmp1)

# with open("./tmp2.v","w") as f:
#   f.write(tmp2)



# module antisat_{name} (A,KEY,Q);
# parameter n={ic},keyval={keyval};
#  input [n-1:0] A;
#  input [2n-1:0] KEY;
#  output Q,Q1,Q2;
# always @ (*) begin  
#   if ((A == keyval) (A == KEY[n-1:0])) begin Q1 = 1; end
#   else begin Q1 = 0; end 
#   if (A == KEY[2n-1:n]) begin Q2 = 1; end
#   else begin Q2 = 0; end  
# end 

# Q=Q1 and Q2;

# endmodule



# import src.utils as utils
# import re
# from satattack.cmd_sat import *



# from z3 import *

# lk = [Bool("a_0"), Bool("a_1"), Bool("a_2")]

# s = Solver()

# for i in lk:
#   s.add(i == False)

# print(s.check())
# print(s.model())




# attack = SatAttack("./tmp2.v","./tmporg.v","v")
# start = time.time()
# attack.run()
# SAT_extecution_time = time.time()-start





# import csv

# with open('log.csv', 'w') as f:
#     f.write("")

# for kx in range(3):
#     to_csv = [
        
# {'bin': '1', 'int': 1, 'len': 1, 'inputs': ['N135']},
# {'bin': '1', 'int': 1, 'len': 1, 'inputs': ['N135']}
#     ]

#     keys = to_csv[0].keys()

#     with open('log.csv', 'a', newline='') as f:
#         dict_writer = csv.DictWriter(f, keys)
#         f.write(str(kx)+"\n")
#         dict_writer.writeheader()
#         dict_writer.writerows(to_csv)




# def verilog_to_bench(verilog):
#     verilog = utils.format_verilog(verilog)
#     inputs,_=utils.extract_io_v(verilog,mode="input")
#     outputs,_=utils.extract_io_v(verilog,mode="output")

#     gates,gate_count = utils.extract_gates_v(verilog)
    
    
#     bench=""
#     for i in inputs:
#         bench+="INPUT({})".format(i)
#     # print(bench)
#     # print(gates)
#     return bench








# # "./linux/assign_tech.v"
# # "./tmporg.v"
# verilog=open("./tmp2.v").read()
# # verilog=utils.format_verilog(verilog)


# inputs,_=utils.extract_io_v(verilog,mode="input")
# outputs,_=utils.extract_io_v(verilog,mode="output")


# t=re.findall("assign (.*) = (.*);",verilog)
# verilog=re.sub("wire.*;\n","",verilog)
# verilog=re.sub("assign (.*) = (.*) ?;\n",r"BUF_g _node(\1)_ ( .A(\2), .Y(\1) );\n",verilog)



# with open("./tmptmp.v","w") as f:
#   f.write(verilog)



# t=re.findall("assign (.*) = (.*);",verilog)
# verilog=re.sub("wire.*;\n","",verilog)
# for i in t:
#   tmpassign=re.findall(utils.text_to_pattern(i[0]),verilog)
#   if("{" in i[0]):
#     tmpi0=i[0][1:-1].split(",")
#     for i in tmpi0:
#       print(i.strip(),end="")
#     print()
#   else:
#     verilog=re.sub(".*"+utils.text_to_pattern(i[0])+".*;\n","",verilog)
#     if(len(tmpassign)==1):
#       if(i[1] in inputs):
#         tmpx=re.findall(utils.text_to_pattern(i[0]),verilog)
#         if(tmpx!=[]):
#           print("inp",i)
#       elif(i[0] in outputs):
#         tmpx=re.findall(utils.text_to_pattern(i[0]),verilog)
#         if(tmpx!=[]):
#           print("out",i)
#       else:
#         pass
#     else:
#       tmpx=re.findall(utils.text_to_pattern(i[0]),verilog)
#       if(tmpx!=[]):
#           print("other ",i,tmpx)

   
