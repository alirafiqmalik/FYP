
from src.utils import randKey, gencc_AntiSAT,gencc_SarLock, hammingcc, io_port,gen_busport
from src.utils import extract_io_v,extract_gates_v,extract_gates_va
from src.utils import sortio,format_verilog,format_bench
from src.conv import bench_to_verilog
from satattack.cmd_sat import *
from src.netlist import *
from src.cmds import *
import subprocess
import random
import time
import csv
import os

# class ReadNetlist:
#   def __init__(self,path):
#     netlist=open(path).read()
#     self.netlist=format_verilog(netlist,remove_wire=True)
#     self.inputs,_=extract_io_v(self.netlist,mode="input")
#     self.outputs,_=extract_io_v(self.netlist,mode="output")




class PostSAT_LL:
  def __init__(self,netlist,mode="verilog"):
    if(mode=="verilog"):
      # self.netlist=netlist
      self.netlist=format_verilog(netlist,remove_wire=True)
      self.inputs,_=extract_io_v(self.netlist,mode="input")
      self.outputs,_=extract_io_v(self.netlist,mode="output")
      self.netlist=re.sub(r"module .* ?\((.*)\);",r"module org (\1);",self.netlist)
      # if("assign" in verilog):
      #   self.gates,self.gate_count=extract_gates_v(self.netlist)
      # else:
      #   self.gates,self.gate_count=extract_gates_va(self.netlist)

      self.logval={}
      self.info()

    # elif(mode=="bench"):
    #   self.netlist=format_bench(netlist)
    #   self.inputs=extract_io_b(self.netlist,mode="input")
    #   self.outputs=extract_io_b(self.netlist,mode="output")
    #   self.gates,self.gate_count=extract_gates_b(self.netlist)

  def info(self)->None:
    print("Number of Inputs = ",len(self.inputs))
    print("Number of Outputs = ",len(self.outputs))
    # print("Total Gates Count  = ",self.gate_count)

  def AntiSat(self,key_lengthi=None):    
    if(key_lengthi==None):
      inputs_key=self.inputs
    else:
      inputs_key=random.sample(self.inputs, key_lengthi)

    keyport=gen_busport("keyinput",2*len(inputs_key))
    iportnodes, inputnodes,_ = io_port(self.inputs)
    oportnodes, outputnodes,_ = io_port(self.outputs,mode="output")

    tmporgport=""
    tmpx=""
    for i in self.outputs:
      if("[" in i):
        outorgi=re.sub(r"\[","_org[",i)
      else:
        outorgi=i+"_org"
        
      tmpx+="assign {} = {} ^ FC;\n".format(i,outorgi)

    for i in iportnodes.split(","):
      tmporgport+=".{}({}),".format(i,i)
    for i in oportnodes.split(","):
      tmporgport+=".{}({}),".format(i,i+"_org")

    self.logval["inputs"]=inputs_key
    self.logval["len"]=key_lengthi
    tmporgport=tmporgport[:-1]

    orgoutputwires=re.sub("output","wire",re.sub(";","_org;",outputnodes))

    corrupt,portnodes_antisat,pc=gencc_AntiSAT("antisat_top", inputs_key)


    # m c,m dx,m

    top="module top({topbus});\n{topio}\n{CRwire}\n{orgmodule}\n{CRmodule}\n{Xornet}\nendmodule"
    top=top.format(
                    topbus=iportnodes+","+oportnodes+","+keyport,
                    topio="input {};\n{}\n{}\n".format(keyport,inputnodes,outputnodes),
                    CRwire=orgoutputwires+"wire {};\n".format("FC"),
                    orgmodule="\norg o1({});".format(tmporgport),
                    CRmodule=pc.format(init="to",portnodes="{%s}"%portnodes_antisat,KEY="{%s}"%keyport,Q="FC"),
                    Xornet=tmpx
                    )

    return top+"\n\n{}\n\n{}".format(corrupt,self.netlist)
    
  
   
  def SarLock(self,key=None,key_lengthi=None,log=False):
    if(key_lengthi==None):
      inputs_key=self.inputs
    else:
      inputs_key=random.sample(self.inputs, key_lengthi)
    
    key_length=len(inputs_key)
    if (key == None):
      key, tmpkey = randKey(key_length)
    else:
      tmpkey=format(key, "0"+str(key_length)+"b")

    keyport=gen_busport("keyinput",len(inputs_key))
    iportnodes, inputnodes,_ = io_port(self.inputs)
    oportnodes, outputnodes,_ = io_port(self.outputs,mode="output")


    if(log):
      self.logval={"bin":tmpkey,"int":key,"len":len(tmpkey),"inputs":inputs_key}
    else:
      print("\n\nGENERATING LOCKING COMPARATORS:")
      print("\tNode Input Length = ",len(self.inputs))
      print("\tKey Length = ",len(tmpkey))
      print("\tKey Value in Int = ",key,"<",2**key_length)
      print("\tKey Value in Binary = ", tmpkey, "\n")

    tmporgport=""
    tmpx=""
    for i in self.outputs:
      if("[" in i):
        outorgi=re.sub(r"\[","_org[",i)
      else:
        outorgi=i+"_org"
        
      tmpx+="assign {} = {} ^ FC;\n".format(i,outorgi)

    for i in iportnodes.split(","):
      tmporgport+=".{}({}),".format(i,i)
    for i in oportnodes.split(","):
      tmporgport+=".{}({}),".format(i,i+"_org")

    self.logval["inputs"]=inputs_key
    self.logval["len"]=key_lengthi
    tmporgport=tmporgport[:-1]

    orgoutputwires=re.sub("output","wire",re.sub(";","_org;",outputnodes))

    corrupt,portnodes_antisat,pc=gencc_SarLock("sarlock_top",inputs_key,key)


    # m c,m dx,m

    top="module top({topbus});\n{topio}\n{CRwire}\n{orgmodule}\n{CRmodule}\n{Xornet}\nendmodule"
    top=top.format(
                    topbus=iportnodes+","+oportnodes+","+keyport,
                    topio="input {};\n{}\n{}\n".format(keyport,inputnodes,outputnodes),
                    CRwire=orgoutputwires+"wire {};\n".format("FC"),
                    orgmodule="\norg o1({});".format(tmporgport),
                    CRmodule=pc.format(init="to",portnodes="{%s}"%portnodes_antisat,KEY="{%s}"%keyport,Q="FC"),
                    Xornet=tmpx
                    )

    return top+"\n\n{}\n\n{}".format(corrupt,self.netlist)


  def getCRunits(self, key, HD=0,key_length=None):  # 734
    if(key_length==None):
      tmp=self.inputs
    else:
      tmp=random.sample(self.inputs, key_length)

    # tmp,outnode=circuit.MaxInputCone()
    cc= hammingcc("corrupt",tmp,HD,key)
    rsc=hammingcc("restore",tmp,HD,None)
    # cc = gencc("corrupt", tmp, key)
    # rsc = gencc("restore", tmp, None)
    # print(cc)
    return tmp,cc, rsc
 
  def SFLL(self,HD=0,key=None,key_lengthi=None,log=False):
    if(key_lengthi==None):
      key_length=len(self.inputs)
    else:
      key_length=key_lengthi
    
    if (key == None):
      key, tmpkey = randKey(key_length)
    else:
      tmpkey=format(key, "0"+str(key_length)+"b")
    
    inputs_key,(corrupt,_,pc),(restore,_,rc)=self.getCRunits(key=key,HD=HD,key_length=key_lengthi)
    keyport=gen_busport("keyinput",len(inputs_key))
    

    if(log):
      self.logval={"bin":tmpkey,"int":key,"len":len(tmpkey),"inputs":inputs_key}
    else:
      print("\n\nGENERATING LOCKING COMPARATORS:")
      print("\tNode Input Length = ",len(self.inputs))
      print("\tKey Length = ",len(tmpkey))
      print("\tKey Value in Int = ",key,"<",2**key_length)
      print("\tKey Value in Binary = ", tmpkey, "\n")
      

    iportnodes, inputnodes,_ = io_port(self.inputs)
    oportnodes, outputnodes,_ = io_port(self.outputs,mode="output")


    tmporgport=""
    tmpx=""
    for i in self.outputs:
      if("[" in i):
        outorgi=re.sub(r"\[","_org[",i)
      else:
        outorgi=i+"_org"
        
      tmpx+="assign {} = {} ^ FC ^ FR;\n".format(i,outorgi)
 
    for i in iportnodes.split(","):
      tmporgport+=".{}({}),".format(i,i)
    for i in oportnodes.split(","):
      tmporgport+=".{}({}),".format(i,i+"_org")
    #tmporgport+=".{}({}),".format(i,i+"")

    # for i in self.inputs:
    #   tmporgport+=".{}({}),".format(i,i+"")

    tmporgport=tmporgport[:-1]

    orgoutputwires=re.sub("output","wire",re.sub(";","_org;",outputnodes))

    top="module top({topbus});\n{topio}\n{CRwire}\n{orgmodule}\n{CRmodule}\n{Xornet}\nendmodule"
    top=top.format(
                   topbus=iportnodes+","+oportnodes+","+keyport,
                   topio="input {};\n{}\n{}\n".format(keyport,inputnodes,outputnodes),
                   CRwire=orgoutputwires+"wire {},{};\n".format("FR","FC"),
                   orgmodule="\norg o1({});".format(tmporgport),
                   CRmodule=pc.format(init="to",Q="FC")+"\n"+rc.format(init="ro",
                   key="{%s}"%keyport,
                   Q="FR"),
                   Xornet=tmpx
                   )

    return top+"\n\n{}\n\n{}\n\n{}".format(corrupt,restore,self.netlist)

  def get_log(self):
    return self.logval


cmds="""
/home/alira/FYP/linux/yosys/build/yosys -q -p'
read_verilog {} 
hierarchy -check -top {}
flatten
proc; opt; fsm; opt; memory; opt;
techmap; opt
# dfflibmap -liberty /home/alira/FYP/vlib/mycells.lib
abc -liberty /home/alira/FYP/vlib/mycells.lib
clean
write_verilog -noattr {}
'
"""


if __name__=="__main__":
  # verilog=open("/home/alira/FYP/linux/assign_tech.v").read()
  # bench=open("/home/alira/FYP/bench/comb/apex2.bench").read()
  # bench=format_bench(bench)
  # verilog,tmp=bench_to_verilog(bench)
  orgdir="/home/alira/FYP/Benchmarks/ISCAS85/"
  # orgpath="/home/alira/FYP/Benchmarks/ISCAS85/c17/c17.v"
  # orgname=orgpath.split("/")[-1][:-2]


  # orgpath=orgdir+"{orgname}/{orgname}.v".format(orgname="c17")
  # verilog=open(orgpath).read()

  # LL=PostSAT_LL(verilog)

  # lockedcir=LL.AntiSat()
  # logval=LL.get_log()
  # with open("./tmptop.v","w") as f:
  #   f.write(lockedcir)
  
  
  with open('log.csv', 'w') as f:
      f.write("")


  count=0
  
  for files in os.listdir(orgdir):
    count=count+1
    if(count==5):
      break
    orgname=files
    
    if(orgname=="c2670"):#"c5315" "c17" "c2670"
      # pass
      break
      # continue

    print("------------------------- Evaluating Security Verification Parameters for {} -------------------------".format(orgname))

    orgpath=orgdir+"{orgname}/{orgname}.v".format(orgname=orgname)

    verilog=open(orgpath).read()
    

    LL=PostSAT_LL(verilog)
    with open("./tmp.v","w") as f:
      f.write(LL.netlist)

    LogFile=[]
    for n in range(1,2):
      start = time.time()
      keylen=n
      print("#########################################################################")
      print("Keylength = ",keylen)

      if(keylen>len(LL.inputs)):
        print("Key length greater than Number of Inputs, Exiting Loop")
        break
      
      lockedcir=LL.SarLock(key_lengthi=keylen,log=True)#LL.SFLL(key_lengthi=keylen,log=True,HD=1)


      logval=LL.get_log()
      with open("./tmptop.v","w") as f:
        f.write(lockedcir)
      
      
      print(logval)
      
      subprocess.run(cmds.format("./tmptop.v","top","./tmp2.v"),shell=True)
      subprocess.run(cmds.format(orgpath,orgname,"./tmporg.v"),shell=True)

      verilog=open("/home/alira/FYP/tmp2.v").read()
      verilog=format_verilog(verilog,remove_wire=True)
      verilog=re.sub("assign (.*) = (.*) ?;\n",r"BUF_g _node_\1_ ( .A(\2), .Y(\1) );\n",verilog)

      with open("./tmp2.v","w") as f:
        f.write(verilog)


      verilog2=open("/home/alira/FYP/tmporg.v").read()
      verilog2=format_verilog(verilog2,remove_wire=True)
      verilog2=re.sub("assign (.*) = (.*) ?;\n",r"BUF_g _node_\1_ ( .A(\2), .Y(\1) );\n",verilog2)

      with open("/home/alira/FYP/tmporg.v","w") as f:
        f.write(verilog2)

      locking_time = time.time()-start
      
      attack = SatAttack("./tmp2.v","./tmporg.v","v")
      start = time.time()
      attack.run()
      SAT_extecution_time = time.time()-start


      tmpk=""
      tmpkeys=list(attack.key)
      tmpkeys.sort(key=lambda x: re.findall(r"\d+",x)[0])
      for i in tmpkeys:
        tmpk='1' if(attack.key[i]) else '0' + tmpk
    
        
        

      logval["attack_iterations"]=attack.iterations
      logval["SAT_keyval"]=tmpk
      logval["locking_time"]=locking_time
      logval["SAT_extecution_time"]=SAT_extecution_time
      
      print(logval)

      LogFile.append(logval)
      

    print("Saving Log for file {}".format(orgname))
    with open('log.csv', 'a', newline='') as f:
      dict_writer = csv.DictWriter(f, LogFile[0].keys())
      f.write(orgname+" ,Number of Inputs = "+str(len(LL.inputs))+" \n")
      dict_writer.writeheader()
      dict_writer.writerows(LogFile)



    


