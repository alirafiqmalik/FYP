from src.LL import LogicLocking as LL

# bench=open("/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1.bench").read()
# bench=open("/home/alira/FYP/tmp.bench").read()
# tmp=LL(netlist=bench)


# t=tmp.outputnodes()

# print("C1_DATA3_0FQ" in t)

# tx=tmp.FindConeinputs(node="C1_DATA3_0FQ")

# print(tx)

# "C1_DATA3_0FQ"


# for i in t:
#   tx=tmp.FindConeinputs(node="o_addr_13_")

#   if(i in tx):
#     print(i)










# import re

# verilog_gates=['BUF','NOT_g', 'AND_g', 'OR_g', 'NAND_g', 'NOR_g','XOR_g','XNOR_g']

# def extract_gates_v(verilog):
#   tmp={}
#   gate_count = {}
# #   tmp[re.sub("_g","",verilog_gates[0])]=re.findall(" "+verilog_gates[0] +" .* \( .A\((.*)\), .Y\((.*)\) \) ?;",verilog)
# #   gate_count[verilog_gates[0]] = len(tmp[re.sub("_g","",verilog_gates[0])])
# #   tmp[re.sub("_g","",verilog_gates[1])]=re.findall(" "+verilog_gates[1] +" .* \( .A\((.*)\), .Y\((.*)\) \) ?;",verilog)
# #   gate_count[verilog_gates[1]] = len(tmp[re.sub("_g","",verilog_gates[1])])

#   for i in verilog_gates:
#     if(i=="NOT_g"):
#         tmpx=re.findall(" "+verilog_gates[0] +" .* \( .A\((.*)\), .Y\((.*)\) \) ?;",verilog)
#     elif(i=="BUF_g"):
#         tmpx=re.findall(" "+verilog_gates[1] +" .* \( .A\((.*)\), .Y\((.*)\) \) ?;",verilog)
#     else:
#         tmpx=re.findall(" "+i +" .* \( .A\((.*)\), .B\((.*)\), .Y\((.*)\) \) ?;",verilog)

#     if(tmpx!=[]):    
#         tmpi=re.sub("_g","",i)
#         tmp[tmpi]=tmpx
#         gate_count[i] = len(tmp[tmpi])
    
#   return tmp,gate_count



# verilog=open("/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1_netlist.v").read()

# lib=open("/home/alira/FYP/linux/CSAW/modulefiles.v").read()


# for i in re.findall("module (.*) ?\((.*)\);",lib):
#   print(i)


# tmp=re.findall("( .*" +" .* \( \..*\((.*)\), \..*\((.*)\), \..*\((.*)\) \) ?;)",verilog)[:2]
# print(tmp)

# python3 /home/alira/FYP/sat_attack/run.py /home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1.bench /home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/oracle1.bench b