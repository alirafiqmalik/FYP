from utils import *
from conv import *
from LL import LogicLocking



bench=open("/home/alira/FYP/python/tmpcir.bench").read()
# circuit=LogicLocking(bench)

# key=randKey(10, seed=10)
# print(key)
# circuit.RLL(n=10, key=key[0])

# circuit.graph_to_bench("/home/alira/FYP/tmp/tmp.bench")



# tmp=extract_gates_b(bench)

# print(tmp[0].keys())
# print(tmp[1])

verilog,r=bench_to_verilog(bench)
print(r)

with open("/home/alira/FYP/tmp/tmporg.v","w") as f:
    f.write(verilog)

# print(gate_count)

