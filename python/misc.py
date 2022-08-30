# class Netlist():
#   def __init__(self,netlist):

#     self.inputs=re.findall("INPUT\((.*)\)\n",netlist)
#     self.outputs=re.findall("OUTPUT\((.*)\)\n",netlist)
    
#     self.circuitgraph = nx.DiGraph()

#     self.wires=[]

#     self.gates={'NOT': 0, 'AND': 0, 'OR': 0, 'NAND': 0, 'NOR': 0,'XNOR':0,'XOR':0}
#     self.keygates={'XOR':0,'XNOR':0}
#     self.keygatescount=0
#     for i in self.gates.keys():
#       if i=='NOT':
#         tmp=re.findall("(.*) = "+ i +"\((.*)\)\n?",netlist)
#         for count,j in enumerate(tmp):
#           #print(j)
#           self.circuitgraph.add_edge("NOT_"+str(count),j[0].strip())
#           self.circuitgraph.add_edge(j[1].strip(),"NOT_"+str(count))
#           for k in j:
#             if( (k not in self.inputs) and (k not in self.outputs) and (k not in self.wires) ):
#               self.wires.append(k)
#               #print(k)
#       else:
#         tmp=re.findall("(.*) = "+ i +"\((.*),(.*)\)\n?",netlist)
#         for count,j in enumerate(tmp):
#           #print(j)
#           self.circuitgraph.add_edge(i+"_"+str(count),j[0].strip())
#           self.circuitgraph.add_edge(j[1].strip(),i+"_"+str(count))
#           self.circuitgraph.add_edge(j[2].strip(),i+"_"+str(count))
#           for k in j:
#             if( (k.strip() not in self.inputs) and (k.strip() not in self.outputs) and (k.strip() not in self.wires) ):
#               self.wires.append(k.strip())
#               #print(k)

#       self.gates[i]+=len(tmp)
#       if(i in self.keygates):
#         self.keygates[i]+=1
      
      
#       #print('count of '+i+" = ",len(tmp))
#       #print(tmp[0])
#     self.wires.sort()
#     self.info()
    
#   def info(self):
#     self.gatecount=0
#     for i in self.gates.keys():
#       self.gatecount+=self.gates[i]
#     print("Gate Nodes   = ",self.gates)
#     print("Total Gates  = ",self.gatecount)
#     print("Total Wires  = ",len(self.wires))
#     print("Input Nodes  = ",len(self.inputs))
#     print("Output Nodes = ",len(self.outputs))
#     print("Total Nodes  = ",int(self.circuitgraph.number_of_nodes()))
#     print("Gates + Wires + Inputs + Outputs = ",self.gatecount + len(self.wires) + len(self.inputs) + len(self.outputs))
  
#   def graph(self):
#     return self.circuitgraph
  
#   def inputnodes(self):
#     return self.inputs
  
#   def outputnodes(self):
#     return self.outputs
  
#   def gatenodes(self):
#     return self.gates
  
#   def wirenodes(self):
#     return self.wires  #wires

#   def nodeio(self,Node):
#     print("Node outputs = ",list(self.circuitgraph.successors(Node))) 
#     print("Node inputs = ",list(self.circuitgraph.predecessors(Node)))
  
#   # def generatekey(self,keyval):
#   #   self.keyval=keyval
#   #   self.keybit=bitarray(keyval)
#   #   print(self.keyval,self.keybit)
#   #   pass

#   def InsertKeyGate(self,NodeA,NodeB,gatetype='XOR'):
#     keygatecount=self.keygates[gatetype]
#     keygate=gatetype+"_"+str(keygatecount)
#     self.circuitgraph.remove_edge(NodeA, NodeB)
#     #len(self.wires) #_0392_
#     keywire="KEY"+str(len(self.wires))
#     self.circuitgraph.add_edge(NodeA,keywire)#keygate)
#     self.circuitgraph.add_edge(keywire,keygate)
#     self.circuitgraph.add_edge(keygate,NodeB)
    
#     self.circuitgraph.add_edge("KEY["+str(self.keygatescount)+"]",keygate)
#     self.inputs.append("KEY["+str(self.keygatescount)+"]")
#     self.wires.append(keywire)
#     self.gates[gatetype]+=1
#     self.keygates[gatetype]+=1
#     self.gatecount+=1
#     self.keygatescount+=1

 
#   def RLL(self,n,key):
#     bitkey=format(key, "b")
#     print(2**n,"<----->",key,"<----->",(2**n)>=key)
#     if(n>len(bitkey)):
#       for i in range(n-len(bitkey)):
#         bitkey='0'+bitkey
#       print("######################################",end="\n          ")
#       print("n > Bits")
#       print(key," ----------> ",bitkey)
#       print("######################################")
#     elif(n<len(bitkey)):
#       print("ERROR")
#       print("Number of Gates < Number of Key-Bits")
#       return None
#     else:
#       print("######################################",end="\n          ")
#       print("n == Bits")
#       print(key," ----------> ",bitkey)
#       print("######################################")

#     random.seed(10)
#     for i in range(n):
#       tp=random.randint(0, len(self.wires)-1)  
#       inp=list(self.circuitgraph.predecessors(self.wires[tp]))
#       #out=list(graph.successors(wires[tp]))
#       #print(wires[tp])
#       #for j in range(1,len(bitkey)+1):  
#       if(bitkey[-(i+1)]=='1'):
#         self.InsertKeyGate(inp[0],self.wires[tp],'XNOR')
#       else:
#         self.InsertKeyGate(inp[0],self.wires[tp],'XOR')
  

#   def graph_to_bench(self,outpath):
#     graphtonetlist=""
#     for i in self.inputnodes():
#       graphtonetlist+="INPUT("+i+")"+"\n"
#       #print("INPUT("+i+")")
    
#     for i in self.outputnodes():
#       #print("OUPUT("+i+")")
#       graphtonetlist+="OUTPUT("+i+")"+"\n"
#     for i in self.gatenodes().keys():
#       for j in range(self.gatenodes()[i]):
#         tmpj=i+"_"+str(j)
#         inp=list(self.circuitgraph.predecessors(tmpj))
#         out=list(self.circuitgraph.successors(tmpj))
#         if(i=="NOT"):
#           graphtonetlist+=out[0]+" = "+i+"("+inp[0]+")"+"\n"
#         else:
#           graphtonetlist+=out[0]+" = "+i+"("+inp[0]+","+inp[1]+")"+"\n"
#     print("Writing BENCH File to Location: ",os.path.join(outpath,"output.bench"))
#     with open(os.path.join(outpath,"output.bench"), 'w') as f:
#       f.write(graphtonetlist)

