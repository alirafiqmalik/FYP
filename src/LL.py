from src.netlist import *
import subprocess
from src.utils import sortio, randKey, gencc, hammingcc,format_verilog, io_port,gen_busport,extract_io_v,extract_gates_va,gate_to_assign
from src.cmds import *
import random

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

# from src.LL import LogicLocking
# from src.utils import bench_to_verilog


# b=open("/home/alira/FYP/linux/MSATLL/benchmarks/original/apex4.bench").read()
# tmp=LogicLocking(b)
# tmp.SLL(10,75)
# tmp.graph_to_bench("/home/alira/FYP/tmp/tmp_sll.bench")

# bl=open("/home/alira/FYP/tmp/tmp_sll.bench").read()

# to,_=bench_to_verilog(b)
# with open("/home/alira/FYP/tmp/tmp_org.v",'w') as f:
#   f.write(to)

# t1,_=bench_to_verilog(bl)
# with open("/home/alira/FYP/tmp/tmp_sll.v",'w') as f:
#   f.write(t1)


class LogicLocking(Netlist):
    def __init__(self, netlist: str) -> None:
        super().__init__(netlist)
        self.keygates = {'XOR': 0, 'XNOR': 0}
        self.keygatescount = 0
        

    def keynodes(self) -> dict:
        return self.keygates


    def InsertKeyGate(self, NodeA: str, NodeB: str, gatetype: str = 'XOR') -> None:
        keygatecount = self.gates[gatetype]
        keygate = gatetype+"_"+str(keygatecount)

        self.circuitgraph.remove_edge(NodeA, NodeB)

        # keywire = "KEY"+str(len(self.wires))
        keywire = "keywire"+str(len(self.wires))

        self.circuitgraph.add_edge(NodeA, keywire)
        self.circuitgraph.add_edge(keywire, keygate)
        self.circuitgraph.add_edge(keygate, NodeB)

        # self.circuitgraph.add_edge("KEY["+str(self.keygatescount)+"]", keygate)
        # self.inputs.append("KEY["+str(self.keygatescount)+"]")

        self.circuitgraph.add_edge("keyinput_"+str(self.keygatescount), keygate)
        self.inputs.append("keyinput_"+str(self.keygatescount))

        self.wires.append(keywire)

        self.gates[gatetype] += 1
        self.gatecount += 1

        self.keygates[gatetype] += 1
        self.keygatescount += 1
    

    

    def RLL(self, n: int, key: int):
        bitkey = format(key, "b")
        print(2**n, "<----->", key, "<----->", (2**n) >= key)
        if (n > len(bitkey)):
            bitkey = format(key, "0"+str(n)+"b")
        elif (n < len(bitkey)):
            print("ERROR")
            print("Number of Gates < Number of Key-Bits")
            return None
        # else:
        print("n == Bits")

        print("######################################", end="\n          ")
        print(key, " ----------> ", bitkey)
        print("######################################")

        random.seed(10)
        i=-1
        while(1):
        # for i in range(n):
            if(i==(n-1)):
                break
            else:
                i+=1
            tp = random.randint(0, len(self.wires)-1)
            inp = list(self.circuitgraph.predecessors(self.wires[tp]))
            if (bitkey[-(i+1)] == '1'):
                self.InsertKeyGate(inp[0], self.wires[tp], 'XNOR')
            elif(len(inp)==0):
                pass
            else:
                self.InsertKeyGate(inp[0], self.wires[tp], 'XOR')
            # print("HERE  ",inp[0],i)
            

    def SLL(self, n: int, key: int):
        bitkey = format(key, "b")
        print(2**n, "<----->", key, "<----->", (2**n) >= key)
        if (n > len(bitkey)):
            bitkey = format(key, "0"+str(n)+"b")
        elif (n < len(bitkey)):
            print("ERROR")
            print("Number of Gates < Number of Key-Bits")
            return None
        # else:
        print("n == Bits")

        print("######################################", end="\n          ")
        print(key, " ----------> ", bitkey)
        print("######################################")

        random.seed(10)
        for i in range(n):
            tp = random.randint(0, len(self.wires)-1)
            inp = list(self.circuitgraph.predecessors(self.wires[tp]))
            if (bitkey[-(i+1)] == '1'):
                pass
                self.InsertKeyGate(inp[0], self.wires[tp], 'XNOR')
            else:
                self.InsertKeyGate(inp[0], self.wires[tp], 'XOR')




    def FindConeinputs(self, node):
        if node in self.inputs:
            return [node]
        # elif (node in [circuit.FFnodes()]):
        else:
            coneinputnode = []
            pred = self.circuitgraph.predecessors(node)
            for i in pred:
                coneinputnode = list(set(coneinputnode) |
                                     set(self.FindConeinputs(i)))
            return coneinputnode

    def MaxInputCone(self):
        maxcount = 0
        maxtmp = []
        maxout = ""
        for i in self.outputs:
            tmp = self.FindConeinputs((i))
            if (len(tmp) > maxcount):
                maxcount = len(tmp)
                maxtmp = tmp
                maxout = i
        return maxtmp, maxout
    

    def graph_to_bench(self) -> str:
        
        graphtonetlist = ""
        for i in self.inputs:
            graphtonetlist += "INPUT("+i+")"+"\n"
            # graphtonetlist +="input {}\n".format(i)

        for i in self.outputs:
            graphtonetlist += "OUTPUT("+i+")"+"\n"
            # graphtonetlist +="output {}\n".format(i)
        

        for i in self.gatenodes().keys():
            for j in range(self.gatenodes()[i]):
                tmpj = i+"_"+str(j)
                inp = list(self.circuitgraph.predecessors(tmpj))
                out = list(self.circuitgraph.successors(tmpj))
                
                if (i == "NOT" or i == 'BUF'):
                    # graphtonetlist += "assign {} = {}{};\n".format(out[0],"~" if i=="NOT" else "",inp[0])
                    graphtonetlist += out[0]+" = "+i+"("+inp[0]+")"+"\n"
                else:
                    # graphtonetlist += "assign {o} = {neg}({i0}{op}{i1});".format(o=out[0],i0=inp[0],i1=inp[1],neg="~" if ((i[0]=="N") or i=="XNOR") else "",op=gate_to_assign[i])
                    graphtonetlist += out[0]+" = "+i + "("+inp[0]+","+inp[1]+")"+"\n"
        return graphtonetlist





# ####################################################################################################################################
# ####################################################################################################################################
# ####################################################################################################################################
# ####################################################################################################################################

# # from src.LL import PostSAT_LL

# # b=open("/home/alira/FYP/tmp.v").read()
# # LL=PostSAT_LL(b,mode="verilog")
# # lockcir=LL.SFLL()

# # with open("/home/alira/FYP/tmptop.v","w") as f:
# #   f.write(lockcir)

# class PostSAT_LL:
#   def __init__(self,netlist,mode):
#     if(mode=="verilog"):
#       #self.netlist=format_verilog(netlist,remove_wire=False)
#       self.netlist=netlist
#       self.inputs,self.ip=extract_io_v(self.netlist,mode="input")
#       # print(getio_v(self.netlist,mode="input"))
#       self.outputs,self.op=extract_io_v(self.netlist,mode="output")
#       self.gates,self.gate_count=extract_gates_va(self.netlist)
#     # elif(mode=="bench"):
#     #   self.netlist=format_bench(netlist)
#     #   self.inputs=extract_io_b(self.netlist,mode="input")
#     #   self.outputs=extract_io_b(self.netlist,mode="output")
#     #   self.gates,self.gate_count=extract_gates_b(self.netlist)

#   def getCRunits(self, key=None, HD=0):  # 734
#     # tmp,outnode=circuit.MaxInputCone()
#     tmp = self.inputs
#     sortio(tmp)
#     if (key == None):
#         key, tmpkey = randKey(len(tmp))
#     else:
#       tmpkey=format(key, "0"+str(len(tmp))+"b")
    
#     print(len(tmp), " ===>> ", len(tmpkey)," ===>> ", 2**len(tmpkey),
#               ">", key, " ===>> ", tmpkey, "\n")
    
#     # cc= hammingcc("corrupt",tmp,HD,key)
#     # rsc=hammingcc("restore",tmp,HD,None)
#     cc = gencc("corrupt", tmp, key)
#     rsc = gencc("restore", tmp, None)
#     return cc, rsc
  
#   def SFLL(self):
#     (corrupt,_,pc),(restore,_,rc)=self.getCRunits(key=102)

#     keyport=gen_busport("keyinput",len(self.inputs))

#     iportnodes, inputnodes,_ = io_port(self.inputs)
#     oportnodes, outputnodes,_ = io_port(self.outputs,mode="output")

#     tmporgport=""
#     tmpx=""
#     for i in self.outputs:
#       tmpx+="assign {} = {} ^ FSR ^ FSO;\n".format(i,i+"org")
#       tmporgport+=".{}({}),".format(i,i+"org")

#     for i in self.inputs:
#       tmporgport+=".{}({}),".format(i,i+"org")

#     tmporgport=tmporgport[:-1]

#     self.netlist=re.sub("module .* ?\((.*)\);",r"module org (\1);",self.netlist)

#     top="module top({topbus});\n{topio}\n{CRwire}\n{orgmodule}\n{CRmodule}\n{Xornet}\nendmodule"
#     top=top.format(topbus=iportnodes+","+oportnodes+","+keyport,topio="input {};\n{}\n{}".format(keyport,inputnodes,outputnodes),CRwire="",orgmodule="org o1({});".format(tmporgport),CRmodule=pc.format(init="to",Q="FSO")+"\n"+rc.format(init="ro",key="{%s}"%keyport,Q="FRO"),Xornet=tmpx)

#     return top+"\n\n{}\n\n{}\n\n{}".format(corrupt,restore,self.netlist)

    