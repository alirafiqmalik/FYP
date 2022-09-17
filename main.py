from src.utils import *
import re


# bench=open("/home/alira/FYP/python/tmpcir.bench").read()
# circuit=LogicLocking(bench)

# key=randKey(10, seed=10)
# print(key)
# circuit.RLL(n=10, key=key[0])

# circuit.graph_to_bench("/home/alira/FYP/tmp/tmp.bench")



# tmp=extract_gates_b(bench)

# print(tmp[0].keys())
# print(tmp[1])



# bench=open("/home/alira/FYP/tmp/tmp.bench").read()
# verilog,r=bench_to_verilog(bench)
# print(r)

# with open("/home/alira/FYP/tmp/obf.v","w") as f:
#     f.write(verilog)



# bench=open("/home/alira/FYP/tmp/tmp.bench").read()
# verilog,r=bench_to_verilog(bench)
# print(r)

# with open("/home/alira/FYP/tmp/tmpobf.v","w") as f:
#     f.write(verilog)


# bench=open("/home/alira/FYP/oracle/oracle.bench").read()
# verilog,r=bench_to_verilog(bench)
# print(r)

# with open("/home/alira/FYP/tmp/tmpobf.v","a") as f:
#     f.write("\n\n\n\n#oracle\n"+verilog)


# "/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/oracle1.bench"
bench=open("/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/design1.bench").read()

def extract_combo_b(bench):
  tmpd=re.findall("(.*) = DFF\((.*)\)",bench)
  txt="#RESTORE DFF VALUES\n"
  for i in tmpd:
    tmpi="{} = DFF({})".format(i[0],i[1])
    txt+=tmpi+"\n"

tmp=re.sub("(.*) = DFF\((.*)\)\n",r"INPUT(\1)\nOUTPUT(\2)\n",bench)


with open("/home/alira/FYP/tmp/combo.bench","w") as f:
    f.write(tmp)


with open("/home/alira/FYP/tmp/seq.bench","w") as f:
    f.write(txt)


# python3 /home/alira/FYP/sat_attack/run.py /home/alira/FYP/tmp/tmprtl.v /home/alira/FYP/tmp/ortl.v
# python3 /home/alira/FYP/sat_attack/run.py /home/alira/FYP/tmp/combo2.bench /home/alira/FYP/tmp/combo.bench