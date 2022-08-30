# **Functions & Classes**

# import matplotlib.pyplot as plt
import networkx as nx
import subprocess
import random
import re


####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

cmd1="""
/home/alira/FYP/linux/yosys/build/yosys -p '
read_verilog {}
hierarchy -check -top top
flatten
{getcpp}write_cxxrtl output.cpp
proc; opt; fsm; opt; memory; opt
techmap; opt
{gettmpv}write_verilog -noattr {}
dfflibmap -liberty /home/alira/FYP/linux/mycells.lib
abc -liberty /home/alira/FYP/linux/mycells.lib
clean
write_verilog -noattr {}
'
"""

cmd2="""
cwd=$(pwd)
#echo $cwd
cd /home/alira/FYP/abc
./abc -c 'read_bench {};write_verilog {}'
cd $cwd
"""

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################


def getnodeport(netlist,buskey):
    tmpval=re.findall(buskey+" (.*);",netlist)
    if(len(tmpval)!=1):
        raise Exception("CHECK "+buskey.upper()+" NODES")
    
    portnodes,busnodes=io_port(tmpval[0].split(", "),mode=buskey) 
    # print(io_port(tmpval[0].split(", ")))
    return portnodes,busnodes

def io_port(inputs,mode="input"):
  tmpdict={}
  for i in inputs:
    if("[" in i and "]" in i):
      tmpis=i.split("[")
      if tmpis[0] in tmpdict:
        tmpdict[tmpis[0]]+=1
      else:
        tmpdict[tmpis[0]]=0
        #print(tmpis[0],tmpis[1][:-1])    
    elif("[" in i or "]" in i):
      print("ERROR INVALID SYNTAX")
    else:
      tmpdict[i]=0  
  
  inputnodes=""
  portnodes=""
  for i in tmpdict.keys():
    portnodes=portnodes+i+","
    if(tmpdict[i]!=0):      
      #print("["+str(tmpdict[i])+":0] "+i)
      inputnodes=inputnodes+mode+" ["+str(tmpdict[i])+":0] "+i+"; "
    else:
      #print(i)
      inputnodes=inputnodes+mode+" "+i+"; "
  
  # inputnodes=inputnodes[:]
  portnodes=portnodes[:-1]
  return portnodes,inputnodes

def sortio(tmp,reverse=True):
  tmpl=list(set([re.sub("\[[0-9]+\]","",i) for i in tmp]))
  tmpl.sort(reverse=False) 
  x=lambda inp: (tmpl.index(re.sub("(\[[0-9]+\])","",inp)),re.sub(".*\[?([0-9]+)\]?.*",r"\1",inp))
  tmp.sort(key=x,reverse=reverse)

def HammingDistance(x:str, y:str)->int:
  h=0
  for i in range(len(x)):
    h+=(x[i]!=y[i])
  return h

def randKey(bits,seed=10):
  random.seed(seed)
  intkey=random.randint(0, (2**bits)-1)
  tmpkey=format(intkey, "0"+str(bits)+"b")
  return intkey,tmpkey

def gencc(modulename,inputs,key):
  ic=len(inputs)
  portnodes,inputnodes=io_port(inputs)
  if(key==None):
    comver="module "+modulename+"("+portnodes+",KEY,Q); "+ inputnodes +"input ["+str(ic-1)+":0]KEY;" + " wire ["+str(ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; always@(*)begin if(A==KEY)Q=1;else Q=0;end endmodule"
  else:
    comver="module "+modulename+"("+portnodes+",Q); "+ inputnodes + " wire ["+str(ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; always@(*)begin if(A=="+str(ic)+"'d"+str(key)+")Q=1;else Q=0;end endmodule"
    
  return re.sub(";",";\n",comver),portnodes


def hammingcc(modulename,inputs,h,key=None):
  ic=len(inputs)
  portnodes,inputnodes=io_port(inputs)
  if(key==None):
    comver="module "+modulename+"("+portnodes+",KEY,Q); "+ inputnodes +"input ["+str(ic-1)+":0]KEY; wire ["+str(ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; integer Qr,count,i; always@(*)begin Qr=KEY^A;count=0; for(i=0;i<"+str(ic)+";i=i+1)begin if(Qr[i]) count=count+1;end if(count=="+str(h)+")Q=1;else Q=0; end endmodule"
  else:
    comver="module "+modulename+"("+portnodes+",Q); "+ inputnodes + " wire ["+str(ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; integer Qr,count,i; always@(*)begin Qr="+str(ic)+"'d"+str(key)+"^A;count=0; for(i=0;i<"+str(ic)+";i=i+1)begin if(Qr[i]) count=count+1;end if(count=="+str(h)+")Q=1;else Q=0; end endmodule"
  return re.sub(";",";\n",comver),portnodes

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################


#netlist=open("/home/alira/FYP/netlist.bench").read()
class Netlist():
  def __init__(self,netlist:str)->None:

    self.inputs=re.findall("INPUT\((.*)\)\n",netlist)
    self.outputs=re.findall("OUTPUT\((.*)\)\n",netlist)
    
    self.circuitgraph = nx.DiGraph()

    self.wires=[]

    self.gates={'BUF': 0,'NOT': 0, 'AND': 0, 'OR': 0, 'NAND': 0, 'NOR': 0,'XNOR':0,'XOR':0}

    self.FFelements={'DFF':0}
  
    for i in self.gates.keys():
      if i=='NOT' or i=='BUF':
        tmp=re.findall("(.*) = "+ i +"\((.*)\)\n?",netlist)
        for count,j in enumerate(tmp):
          #print(j)
          self.circuitgraph.add_edge(i+"_"+str(count),j[0].strip())
          self.circuitgraph.add_edge(j[1].strip(),i+"_"+str(count))
          for k in j:
            tmpk=k.strip()
            if( (tmpk not in self.inputs) and (tmpk not in self.outputs) and (tmpk not in self.wires) ):
              self.wires.append(tmpk)
              #print(k)
      else:
        tmp=re.findall("(.*) = "+ i +"\((.*),(.*)\)\n?",netlist)
        for count,j in enumerate(tmp):
          #print(j)
          self.circuitgraph.add_edge(i+"_"+str(count),j[0].strip())
          self.circuitgraph.add_edge(j[1].strip(),i+"_"+str(count))
          self.circuitgraph.add_edge(j[2].strip(),i+"_"+str(count))
          for k in j:
            tmpk=k.strip()
            if( (tmpk not in self.inputs) and (tmpk not in self.outputs) and (tmpk not in self.wires) ):
              self.wires.append(tmpk)
              #print(k)

      self.gates[i]+=len(tmp)
      
    self.wires.sort()
    self.info()
    
  def info(self)->None:
    self.gatecount=0
    for i in self.gates.keys():
      self.gatecount+=self.gates[i]

    self.FFcount=0
    for i in self.FFelements.keys():
      self.FFcount+=self.FFelements[i]
    print("Gate Nodes   = ",self.gates)
    print("Total Gates  = ",self.gatecount)
    print("Flip-Flop Elements",self.FFelements)
    print("Total Flip-Flop Elements",self.FFcount)
    print("Total Wires  = ",len(self.wires))
    print("Input Nodes  = ",len(self.inputs))
    print("Output Nodes = ",len(self.outputs))
    print("Total Nodes  = ",int(self.circuitgraph.number_of_nodes()))
    print("Gates + Wires + Inputs + Outputs = ",self.gatecount + len(self.wires) + len(self.inputs) + len(self.outputs))
  
  def graph(self):
    return self.circuitgraph
  
  def inputnodes(self)->list:
    return self.inputs
  
  def outputnodes(self)->list:
    return self.outputs
  
  def gatenodes(self)->dict:
    return self.gates
  
  def wirenodes(self)->list:
    return self.wires  #wires

  def FFnodes(self)->dict:
    return self.FFelements

  def nodeio(self,Node)->None:
    print("Node outputs = ",list(self.circuitgraph.successors(Node))) 
    print("Node inputs = ",list(self.circuitgraph.predecessors(Node)))
  
  # def generatekey(self,keyval):
  #   self.keyval=keyval
  #   self.keybit=bitarray(keyval)
  #   print(self.keyval,self.keybit)
  #   pass

  def graph_to_bench(self,outpath:str)->None:
    graphtonetlist=""
    for i in self.inputnodes():
      graphtonetlist+="INPUT("+i+")"+"\n"
      #print("INPUT("+i+")")
    
    for i in self.outputnodes():
      #print("OUPUT("+i+")")
      graphtonetlist+="OUTPUT("+i+")"+"\n"
    for i in self.gatenodes().keys():
      for j in range(self.gatenodes()[i]):
        tmpj=i+"_"+str(j)
        inp=list(self.circuitgraph.predecessors(tmpj))
        out=list(self.circuitgraph.successors(tmpj))
        if(i=="NOT" or i=='BUF'):
          graphtonetlist+=out[0]+" = "+i+"("+inp[0]+")"+"\n"
        else:
          graphtonetlist+=out[0]+" = "+i+"("+inp[0]+","+inp[1]+")"+"\n"
    print("Writing BENCH File to Location: ",outpath)
    with open(outpath, 'w') as f:
      f.write(graphtonetlist)


####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################


class LogicLocking(Netlist):
  def __init__(self,netlist:str)->None:
    super().__init__(netlist)
    self.keygates={'XOR':0,'XNOR':0}
    self.keygatescount=0
    self.FSgates={'XOR':0,'XNOR':0}
    self.FSgatescount=0
    self.FRgates={'XOR':0,'XNOR':0}
    self.FRgatescount=0
    self.FSinputs=[]
    self.FRinputs=[]

  def keynodes(self)->dict:
    return self.keygates

  def FSnodes(self)->dict:
    return self.FSgates

  def FRnodes(self)->dict:
    return self.FRgates

  def InsertFSGate(self,NodeA:str,NodeB:str,gatetype:str ='XOR',)->None:
    FSgatescount=self.gates[gatetype]
    FSgate=gatetype+"_"+str(FSgatescount)

    FRgatescount=FSgatescount+1
    FRgate=gatetype+"_"+str(FRgatescount)

    self.circuitgraph.remove_edge(NodeA, NodeB)
    
    keywireS="FSwire"+str(self.FSgatescount)
    keywireR="FRwire"+str(self.FRgatescount)
    
    self.circuitgraph.add_edge(NodeA,keywireS)
    self.circuitgraph.add_edge(keywireS,FSgate)
    self.circuitgraph.add_edge(FSgate,keywireR)

    self.circuitgraph.add_edge(keywireR,FRgate)

    self.circuitgraph.add_edge(FRgate,NodeB)


    self.circuitgraph.add_edge("FSI_"+str(self.FSgatescount),FSgate)
    self.circuitgraph.add_edge("FRI_"+str(self.FRgatescount),FRgate)
    

    self.FSinputs.append("FSI_"+str(self.FSgatescount))
    self.FRinputs.append("FRI_"+str(self.FRgatescount))
    
    self.wires.append(keywireS)
    self.wires.append(keywireR)
    
    self.gates[gatetype]+=2
    self.gatecount+=2

    self.FSgates[gatetype]+=1
    self.FSgatescount+=1

    self.FRgates[gatetype]+=1
    self.FRgatescount+=1

  def InsertKeyGate(self,NodeA:str,NodeB:str,gatetype:str ='XOR')->None:
    keygatecount=self.gates[gatetype]
    keygate=gatetype+"_"+str(keygatecount)

    self.circuitgraph.remove_edge(NodeA, NodeB)
    
    keywire="KEY"+str(len(self.wires))
    
    self.circuitgraph.add_edge(NodeA,keywire)
    self.circuitgraph.add_edge(keywire,keygate)
    self.circuitgraph.add_edge(keygate,NodeB)

    self.circuitgraph.add_edge("KEY["+str(self.keygatescount)+"]",keygate)
    self.inputs.append("KEY["+str(self.keygatescount)+"]")
    
    self.wires.append(keywire)
    
    self.gates[gatetype]+=1
    self.gatecount+=1

    self.keygates[gatetype]+=1
    self.keygatescount+=1
  
  def RLL(self,n:int,key:int)->list:
    bitkey=format(key, "b")
    print(2**n,"<----->",key,"<----->",(2**n)>=key)
    if(n>len(bitkey)):
      bitkey=format(key, "0"+str(n)+"b")
    elif(n<len(bitkey)):
      print("ERROR")
      print("Number of Gates < Number of Key-Bits")
      return None
    else:
      print("n == Bits")


      print("######################################",end="\n          ")
      print(key," ----------> ",bitkey)
      print("######################################")

    random.seed(10)
    for i in range(n):
      tp=random.randint(0, len(self.wires)-1)  
      inp=list(self.circuitgraph.predecessors(self.wires[tp]))
      if(bitkey[-(i+1)]=='1'):
        self.InsertKeyGate(inp[0],self.wires[tp],'XNOR')
      else:
        self.InsertKeyGate(inp[0],self.wires[tp],'XOR')

  def FindConeinputs(self, node):
    if node in self.inputs:
      return [node] 
    #elif (node in [circuit.FFnodes()]):
    else:
      coneinputnode=[]
      pred=self.circuitgraph.predecessors(node)
      for i in pred:
        coneinputnode=list(set(coneinputnode)|set(self.FindConeinputs(i)))
      return coneinputnode    

  def MaxInputCone(self):
    maxcount=0
    maxtmp=[]
    maxout=""
    for i in self.outputs:
      tmp=self.FindConeinputs((i))
      if(len(tmp)>maxcount):
        maxcount=len(tmp)
        maxtmp=tmp
        maxout=i
    return maxtmp,maxout

  def getCRunits(self,key=None,HD=0):#734
    #tmp,outnode=circuit.MaxInputCone()
    tmp=self.inputs
    sortio(tmp)
    if(key==None):
      key,tmpkey=randKey(len(tmp))
      print(len(tmp)," ===>> ",len(tmpkey)," ===>> ",key," ===>> ",tmpkey,"\n")
    
    #cc= hammingcc("corrupt",tmp,HD,key)
    #rsc=hammingcc("restore",tmp,HD,None)
    cc= gencc("corrupt",tmp,key)
    rsc=gencc("restore",tmp,None)
    return cc,rsc
   
  def SFLLHD(self,outputpath="./output.v",HD=None,key=None):#734
    cctxt,rstx=self.getCRunits(key=key,HD=HD)
    inpnodes=self.inputs
    sortio(inpnodes)
    outnodes=self.outputs
    for coneout in outnodes:
        coneinp=self.FindConeinputs(coneout)
        sortio(coneinp)
        # if(tmp==coneinp):
        tmpi=list(self.circuitgraph.predecessors(coneout))[0]
        self.InsertFSGate(tmpi,coneout)

    keyi=["keyinput"+i for i in inpnodes]
    sortkey=io_port(keyi)
    
    self.graph_to_bench("/home/alira/FYP/output.bench")

    subprocess.run(cmd2.format("/home/alira/FYP/output.bench","/home/alira/FYP/btv_output.v"),shell=True)
    subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/btv_output.v \/home/alira/FYP/output",shell=True)
    netlist=open("/home/alira/FYP/btv_output.v").read()

    tmpx="corrupt C" +"("+cctxt[1]+","+"FSO"+");\nrestore R" +"("+rstx[1]+",{"+sortkey[0]+"},FRO"+");\n"

    for i in range(self.FSnodes()["XOR"]):
        tmpss="FSI_"+str(i)
        tmpsr="FRI_"+str(i)

        tmpx+="assign FSI_"+str(i)+"=FSO;\n"
        tmpx+="assign FRI_"+str(i)+"=FRO;\n"

        netlist=re.sub("input.*"+tmpss+".*;","",netlist)
        netlist=re.sub(tmpss+" ?,","",netlist)

        netlist=re.sub("input.*"+tmpsr+".*;","",netlist)
        netlist=re.sub(tmpsr+" ?,","",netlist)

    tmpx+="endmodule\n"


    netlist=re.sub("(module .*\(.*)(\);)",r"\1,"+sortkey[0]+");"+sortkey[1],netlist)

    netlist=re.sub("\s+"," ",netlist)
    netlist=re.sub(";",";\n",netlist)

    netlist=re.sub("endmodule",tmpx,netlist)
    netlist+="\n\n"+cctxt[0]
    netlist+="\n\n"+rstx[0]

    with open("/home/alira/FYP/input.v", 'w') as f:
        f.write(netlist)

    subprocess.run(cmd1.format("input.v","./tmpoutput.v",outputpath,getcpp="",gettmpv=""),shell=True)
    # print("###################################################\nDONE")
    subprocess.run("python3 /home/alira/FYP/python/misc_vtb_obs.py",shell=True)
    # subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py "+outputpath,shell=True)

  def graph_to_bench(self,outpath:str)->None:
    graphtonetlist=""
    for i in self.inputs:
      graphtonetlist+="INPUT("+i+")"+"\n"
      #print("INPUT("+i+")")
    
    for i in self.FSinputs:
      graphtonetlist+="INPUT("+i+")"+"\n"
    
    for i in self.FRinputs:
      graphtonetlist+="INPUT("+i+")"+"\n"
    
    for i in self.outputs:
      #print("OUPUT("+i+")")
      graphtonetlist+="OUTPUT("+i+")"+"\n"
    for i in self.gatenodes().keys():
      for j in range(self.gatenodes()[i]):
        tmpj=i+"_"+str(j)
        inp=list(self.circuitgraph.predecessors(tmpj))
        out=list(self.circuitgraph.successors(tmpj))
        if(i=="NOT" or i=='BUF'):
          graphtonetlist+=out[0]+" = "+i+"("+inp[0]+")"+"\n"
        else:
          graphtonetlist+=out[0]+" = "+i+"("+inp[0]+","+inp[1]+")"+"\n"
          
    print("Writing BENCH File to Location: ",outpath)
    with open(outpath, 'w') as f:
      f.write(graphtonetlist)




####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################



# #tmp=circuit.FFnodes()
# tmp=circuit.gatenodes()
# FFQ=[]
# FFD=[]
# for i in tmp:
#   #print(i,tmp[i])
#   for j in range(tmp[i]):
#     tp=i+"_"+str(j)
#     FFD=list(set(FFD)|set(graph.predecessors(tp)))
#     FFQ=list(set(FFQ)|set(graph.successors(tp)))
# print(FFD,"\n",FFQ)


# netlist=open("/home/alira/FYP/netlist.bench").read()
# circuit=LogicLocking(netlist)
# graph=circuit.graph()
# circuit.gatenodes()
# wires=circuit.wirenodes()
# circuit.info()

#circuit.InsertKeyGate("AND_480","_0271_")

# tp="_0033_"
# inp=list(graph.predecessors(tp))
# out=list(graph.successors(tp))
# print(inp,out)


# circuit.RLL(n=3,key=3)
# print("HERE")
# circuit.info()




# circuit.graph_to_bench("./output.bench")


# tp1=re.findall("(.*) = "+ "NOR" +"\((.*),(.*)\)\n",netlist)
# tp2=re.findall("(.*) = "+ "OR" +"\((.*),(.*)\)\n",netlist)
# for i in tp1:
#   if i in tp2:
#     print(i)

# #tp=circuit.output()
# tp=circuit.nodes()[1]
# for i in range(len(tp)):
#   print(tp[i])
#   circuit.nodeio(tp[i])
#   print("#####################################")


# for i in wires:
#   if(i=="XNOR_0"):
#     print(i)




# for i in wires:
#   tmp=list(graph.successors(i))
#   if(len(tmp)>7):
#     print(i,len(tmp))



# tp="XNOR_0"
# inp=list(graph.predecessors(tp))
# out=list(graph.successors(tp))
# print(inp,out)





#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################





# cmd1="""
# yosys -p '
# read_verilog input.v
# hierarchy -check -top top
# flatten
# write_cxxrtl output.cpp
# proc; opt; fsm; opt; memory; opt
# techmap; opt
# write_verilog -noattr ./tmpoutput.v
# dfflibmap -liberty yosys/manual/PRESENTATION_Intro/mycells.lib
# abc -liberty yosys/manual/PRESENTATION_Intro/mycells.lib
# clean
# write_verilog -noattr ./output.v
# '
# """


# cmd2="""
# cwd=$(pwd)
# #echo $cwd
# cd /home/alira/FYP/abc
# ./abc -c 'read_bench /home/alira/FYP/output.bench;write_verilog /home/alira/FYP/btv_output.v'
# cd $cwd
# """

# cmd3="""
# yosys -p '
# read_verilog /home/alira/FYP/btv_output.v
# hierarchy -check -top top
# flatten
# proc; opt; fsm; opt; memory; opt
# techmap; opt
# dfflibmap -liberty yosys/manual/PRESENTATION_Intro/mycells.lib
# #abc -genlib libfile.genlib
# abc -liberty yosys/manual/PRESENTATION_Intro/mycells.lib
# clean
# write_verilog -noexpr -noattr /home/alira/FYP/btv_output_yosys.v
# '
# """



# ####################################################################################################################


# cmd4="""
# cwd=$(pwd)
# #echo $cwd
# cd /home/alira/FYP/abc
# ./abc -c 'read_bench /home/alira/FYP/org.bench;write_verilog /home/alira/FYP/btv_org.v'
# cd $cwd
# """
# cmd5="""
# yosys -p '
# read_verilog /home/alira/FYP/btv_org.v
# hierarchy -check -top top
# flatten
# proc; opt; fsm; opt; memory; opt
# techmap; opt
# dfflibmap -liberty yosys/manual/PRESENTATION_Intro/mycells.lib
# #abc -genlib libfile.genlib
# abc -liberty yosys/manual/PRESENTATION_Intro/mycells.lib
# clean
# write_verilog -noexpr -noattr /home/alira/FYP/btv_org_yosys.v
# '
# """