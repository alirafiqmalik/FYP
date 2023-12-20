# import src.verification as verification
import src.utils as utils
import src.conv as conv
import networkx as nx
import src.LL as LL
# import subprocess
# import os
import re

verilog=open("./tmp2.v").read()
bench=conv.verilog_to_bench(verilog)


tmpLL=LL.LogicLocking(bench)



nbits=5
intkey, tmpkey=utils.randKey(nbits)
# tmpLL.RLL(nbits,intkey)
G=tmpLL.circuitgraph
start=tmpLL.inputs[0]


split=intkey

num_inv=tmpLL.gates["NOT"]

# if num_inv < split:
#   ProduceInverters(C,N onInvList,split-num_inv)


def InsertInverter(self, NodeA: str, NodeB: str) -> None:
    gatetype="NOT"
    gatecount = self.gates[gatetype]
    inv_gate = gatetype+"_"+str(gatecount)
    print(NodeA,NodeB)



    self.circuitgraph.remove_edge(NodeA, NodeB)


    invwire_inp = "invwire"+str(len(self.wires))+"_inp"
    invwire_out = "invwire"+str(len(self.wires))+"_out"

    self.circuitgraph.add_edge(NodeA, invwire_inp)
    self.circuitgraph.add_edge(invwire_inp, inv_gate)
    self.circuitgraph.add_edge(inv_gate,invwire_out)
    self.circuitgraph.add_edge(invwire_out,NodeB)

    self.circuitgraph=nx.relabel_nodes(self.circuitgraph,{NodeA:"N"+NodeA+"_new"})
    self.wires.append(invwire_inp)
    self.wires.append(invwire_out)

    self.gates[gatetype] += 1
    self.gatecount += 1

    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



# G=nx.path_graph(3) # nodes 0-1-2
# mapping={}
# H=nx.relabel_nodes(G,mapping)








InsertInverter(tmpLL,list(G.predecessors(tmpLL.outputs[0]))[0], tmpLL.outputs[0])


nx.drawing.nx_agraph.write_dot(tmpLL.circuitgraph, "./tmp.dot")
