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



# print(verilog)
with open("./tmp2.bench", 'w') as f:
  f.write(bench)








tmpLL=LL.LogicLocking(bench)
# tmpLL.nodeio("j")
# tmpLL.nodeio("NAND_1")


nbits=5
intkey, tmpkey=utils.randKey(nbits)
# tmpLL.RLL(nbits,intkey)
G=tmpLL.circuitgraph
start=tmpLL.inputs[0] #N10112


n=10
sources=["_03_"]#tmpLL.outputs#[tmpLL.outputs[0]]

def gentmp2(check):
    
    current_layer = list(sources)
    visited = set(sources)

    for source in current_layer:
        if source not in G:
            raise nx.NetworkXError(f"The node {source} is not in the graph.")

    
    count=1
    while current_layer:
        next_layer = list()
        for node in current_layer:
            #   print("   "+node)
            for child in check(node):#list(G.successors(node)):
                #   print("      "+child)
                if child not in visited:
                    visited.add(child)
                    next_layer.append(child)
        if(~count%2):
            print(current_layer)
        current_layer = next_layer
        count+=1
    
    



# for node_l in current_layer:
#     inp = list(tmpLL.circuitgraph.successors(node_l))
#     # print(node_l,inp[0])
#     # tmpLL.InsertKeyGate(NodeA=node_l, NodeB= inp[0], gatetype= 'XOR')


def gentmp():
    for sources in tmpLL.outputs: 
        sources=[sources]
        print(sources)
        current_layer = list(sources)
        visited = set(sources)
        # layering={i:[] for i in current_layer}

        for source in current_layer:
            if source not in G:
                raise nx.NetworkXError(f"The node {source} is not in the graph.")

        while current_layer:
            next_layer = list()
            for node in current_layer:
                # print("   "+node)
                for child in list(G.predecessors(node)):#list(G.successors(node)):
                    # print("      "+child)
                    if child not in visited:
                        visited.add(child)
                        next_layer.append(child)
            print("   ",current_layer[:2])
            current_layer = next_layer

nx.drawing.nx_agraph.write_dot(G, "./tmpun.dot")
# print(dict(enumerate(gentmp())))
# gentmp()
print("")
gentmp2(lambda x: list(G.predecessors(x)))
print("------------------")
gentmp2(lambda x: list(G.successors(x)))
print("")
# gentmp()
# print("")
# tmpLL.RLL(nbits,intkey)


# gentmp()



nx.drawing.nx_agraph.write_dot(G, "./tmp.dot")

