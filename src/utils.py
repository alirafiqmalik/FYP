import re
import random

#gates=['INVX1', 'AND2X1', 'OR2X1', 'NAND2X1', 'NOR2X1']
#gates=['not_g', 'and_g', 'or_g', 'nand_g', 'nor_g']
#gates=['NOT', 'AND', 'OR', 'NAND', 'NOR']
v_gates_ps="_g"
verilog_gates=['BUF','NOT_g', 'AND_g', 'OR_g', 'NAND_g', 'NOR_g','XOR_g','XNOR_g']
bench_gates=['BUF','NOT', 'AND', 'OR', 'NAND', 'NOR','XOR','XNOR']


####################################################################################################################################
####################################################################################################################################

def merge_lists(listset):
    tmplist=[]
    if(type(listset[0])==list):
        for i in listset:
            tmplist=list(set(tmplist)|set(i))
    return tmplist


####################################################################################################################################
####################################################################################################################################

def getnodeport(netlist, buskey):
    tmpval = re.findall(buskey+" (.*);", netlist)
    if (len(tmpval) != 1):
        raise Exception("CHECK "+buskey.upper()+" NODES")

    portnodes, busnodes = io_port(tmpval[0].split(", "), mode=buskey)
    # print(io_port(tmpval[0].split(", ")))
    return portnodes, busnodes


####################################################################################################################################
####################################################################################################################################

def io_port(inputs, mode="input"):
    tmpdict = {}
    for i in inputs:
        if ("[" in i and "]" in i):
            tmpis = i.split("[")
            if tmpis[0] in tmpdict:
                tmpdict[tmpis[0]] += 1
            else:
                tmpdict[tmpis[0]] = 0
                # print(tmpis[0],tmpis[1][:-1])
        elif ("[" in i or "]" in i):
            print("ERROR INVALID SYNTAX")
        else:
            tmpdict[i] = 0

    inputnodes = ""
    portnodes = ""
    for i in tmpdict.keys():
        portnodes = portnodes+i+","
        if (tmpdict[i] != 0):
            #print("["+str(tmpdict[i])+":0] "+i)
            inputnodes = inputnodes+mode+" ["+str(tmpdict[i])+":0] "+i+"; "
        else:
            # print(i)
            inputnodes = inputnodes+mode+" "+i+"; "

    # inputnodes=inputnodes[:]
    portnodes = portnodes[:-1]
    return portnodes, inputnodes

####################################################################################################################################
####################################################################################################################################


def sortio(tmp, reverse=True):
    tmpl = list(set([re.sub("\[[0-9]+\]", "", i) for i in tmp]))
    tmpl.sort(reverse=False)
    def x(inp): return (tmpl.index(
        re.sub("(\[[0-9]+\])", "", inp)), re.sub(".*\[?([0-9]+)\]?.*", r"\1", inp))
    tmp.sort(key=x, reverse=reverse)

####################################################################################################################################
####################################################################################################################################

def HammingDistance(x: str, y: str) -> int:
    h = 0
    for i in range(len(x)):
        h += (x[i] != y[i])
    return h

####################################################################################################################################
####################################################################################################################################

def randKey(bits, seed=10):
    random.seed(seed)
    intkey = random.randint(0, (2**bits)-1)
    tmpkey = format(intkey, "0"+str(bits)+"b")
    return intkey, tmpkey

####################################################################################################################################
####################################################################################################################################

def gencc(modulename, inputs, key):
    ic = len(inputs)
    portnodes, inputnodes = io_port(inputs)
    if (key == None):
        comver = "module "+modulename+"("+portnodes+",KEY,Q); " + inputnodes + "input ["+str(ic-1)+":0]KEY;" + " wire ["+str(
            ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; always@(*)begin if(A==KEY)Q=1;else Q=0;end endmodule"
    else:
        comver = "module "+modulename+"("+portnodes+",Q); " + inputnodes + " wire ["+str(
            ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; always@(*)begin if(A=="+str(ic)+"'d"+str(key)+")Q=1;else Q=0;end endmodule"

    return re.sub(";", ";\n", comver), portnodes

####################################################################################################################################
####################################################################################################################################


def hammingcc(modulename, inputs, h, key=None):
    ic = len(inputs)
    portnodes, inputnodes = io_port(inputs)
    if (key == None):
        comver = "module "+modulename+"("+portnodes+",KEY,Q); " + inputnodes + "input ["+str(ic-1)+":0]KEY; wire ["+str(
            ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; integer Qr,count,i; always@(*)begin Qr=KEY^A;count=0; for(i=0;i<"+str(ic)+";i=i+1)begin if(Qr[i]) count=count+1;end if(count=="+str(h)+")Q=1;else Q=0; end endmodule"
    else:
        comver = "module "+modulename+"("+portnodes+",Q); " + inputnodes + " wire ["+str(ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; integer Qr,count,i; always@(*)begin Qr="+str(
            ic)+"'d"+str(key)+"^A;count=0; for(i=0;i<"+str(ic)+";i=i+1)begin if(Qr[i]) count=count+1;end if(count=="+str(h)+")Q=1;else Q=0; end endmodule"
    return re.sub(";", ";\n", comver), portnodes


####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################


def format_verilog(netlist,remove_wire=False):
  netlist=re.sub("//.*\n","",netlist)
  netlist=re.sub("[/][*].*[*][/]","",netlist)
  netlist=re.sub("[(][*].*[*][)]\n","",netlist)

  if(remove_wire):
    netlist=re.sub("wire .*;\n","",netlist)

  netlist=re.sub("\n+","",netlist)
  netlist=re.sub("\s+"," ",netlist)
  netlist=re.sub(" ?; ?",";\n",netlist)
  netlist=re.sub("endmodule","endmodule\n",netlist)
  return netlist

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################


def format_bench(netlist):
#   netlist=re.sub("//.*\n","",netlist)
#   netlist=re.sub("[/][*].*[*][/]","",netlist)
#   netlist=re.sub("#.*\n","\n",netlist)

  netlist=re.sub("="," = ",netlist)
  netlist=re.sub("\n+","",netlist)
  netlist=re.sub("\s+"," ",netlist)
  netlist=re.sub("\)",")\n",netlist)

  return netlist


####################################################################################################################################
####################################################################################################################################

def extract_io_b(bench,mode="input"):
    tmp=re.findall(mode.upper()+"\((.*)\)",bench)
    sortio(tmp)
    return tmp

####################################################################################################################################
####################################################################################################################################
def extract_gates_b(bench):
    tmp={i:[] for i in bench_gates}
    gate_count = {i: 0 for i in tmp}
    for i in bench_gates:
        if i=='NOT' or i=='BUF':
            tmp[i]=re.findall(" ?(.*) = "+ i +"\((.*)\)\n?",bench)
        else:
            tmp[i]=re.findall(" ?(.*) = "+ i +"\((.*),(.*)\)\n?",bench)
        
        gcount = len(tmp[i])
        if (gcount == 0):
            tmp.pop(i, None)
        else:
            gate_count[i] = gcount
            

    return tmp,gate_count

####################################################################################################################################
####################################################################################################################################


def dict_to_bin(output,printo=False,reverse=True):
    bin=""
    outkeys=list(output.keys())
    sortio(outkeys,reverse=reverse)
    if(printo):
        print(outkeys)
    for i in outkeys:
        val=output[i] if(type(output[i])==bool) else output[i].value()
        if(val==None):
            return -1
        bin+="1" if val else "0"
    return bin	

####################################################################################################################################
####################################################################################################################################

def bin_to_dict(vdict,bin):
	val=list(vdict.keys())
	tmp={}
	for i in range(len(val)):
		if(type(bin[i])==bool):
			tmp[val[i]]=bin[i]
		else:
			tmp[val[i]]=True if (bin[i]=='1') else False
	return tmp



####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################


def getio_v(verilog,mode="input"):
  tmp=re.findall(mode.lower()+" (.*);",verilog)
  port=""
  nodes=[]
  for i in tmp:
    if(("[" in i) and ("]" in i)):
      tmpi=re.findall("(.*)\[(.*):(.*)]",i)[0]
      port+=tmpi[0]+","
      for j in range(int(tmpi[2]),int(tmpi[1])+1):
        # print(tmpi[0]+"["+str(j)+"]")
        nodes.append(tmpi[0]+"["+str(j)+"]")
    else:
      port+=i+","
      nodes.append(i)
  return nodes,port

####################################################################################################################################
####################################################################################################################################

def extract_gates_v(verilog):
  tmp={}
  gate_count = {}
#   tmp[re.sub("_g","",verilog_gates[0])]=re.findall(" "+verilog_gates[0] +" .* \( .A\((.*)\), .Y\((.*)\) \) ?;",verilog)
#   gate_count[verilog_gates[0]] = len(tmp[re.sub("_g","",verilog_gates[0])])
#   tmp[re.sub("_g","",verilog_gates[1])]=re.findall(" "+verilog_gates[1] +" .* \( .A\((.*)\), .Y\((.*)\) \) ?;",verilog)
#   gate_count[verilog_gates[1]] = len(tmp[re.sub("_g","",verilog_gates[1])])

  for i in verilog_gates:
    if(i=="NOT_g"):
        tmpx=re.findall(" "+verilog_gates[0] +" .* \( .A\((.*)\), .Y\((.*)\) \) ?;",verilog)
    elif(i=="BUF_g"):
        tmpx=re.findall(" "+verilog_gates[1] +" .* \( .A\((.*)\), .Y\((.*)\) \) ?;",verilog)
    else:
        tmpx=re.findall(" "+i +" .* \( .A\((.*)\), .B\((.*)\), .Y\((.*)\) \) ?;",verilog)

    if(tmpx!=[]):    
        tmpi=re.sub("_g","",i)
        tmp[tmpi]=tmpx
        gate_count[i] = len(tmp[tmpi])
    
  return tmp,gate_count


####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################


# def extract_io_v(netlist,mode="input"):
#   for i in re.findall(mode+" .*;\n",netlist):
#     if("[" in i):
#       tmpstr=""
#       tmp=re.findall(mode+" \[(\d+):(\d+)\] (.*);",i)[0]
#       for k in range(int(tmp[1]),int(tmp[0])+1):
#         tmpstr=tmpstr+mode.upper()+"("+tmp[2]+"["+str(k)+"]);"+"\n"
#     else:
#       tmp=i.split(" ")[-1][:-2]
#       tmpstr=mode.upper()+"("+tmp+");"
    
#     tmpi=re.sub("\[","\[",i)
#     tmpi=re.sub("\]","\]",tmpi)
#     netlist=re.sub(tmpi,tmpstr,netlist)
#   netlist=re.sub(r" \[",r"[",netlist)
#   return netlist


# def extract_gates_v(netlist):
    
#     tmp={re.sub("_g","",i):[] for i in verilog_gates}
#     gate_count = {i: 0 for i in tmp}
#     tmp[re.sub("_g","",verilog_gates[2])]=re.findall(r"("+ verilog_gates[2] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",netlist)
#     gate_count[verilog_gates[2]] = len(re.sub("_g","",verilog_gates[2]))
    
#     tmp[re.sub("_g","",verilog_gates[1])]=re.findall(r"("+ verilog_gates[1] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",netlist)
#     gate_count[verilog_gates[1]] += len(re.sub("_g","",verilog_gates[1]))
    
#     tmp[re.sub("_g","",verilog_gates[0])]=re.findall(r"("+ verilog_gates[0] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",netlist)
#     gate_count[verilog_gates[1]] += len(re.sub("_g","",verilog_gates[1]))

#     for i in verilog_gates[3:]:
#         tmp[re.sub("_g","",i)]=re.findall(r"( "+ i +".* \( \.A\()(.*)(\), \.B\()(.*)(\), \.Y\()(.*)(\) \))",netlist)
#         gate_count[re.sub("_g","",i)] = len(tmp[re.sub("_g","",i)])   
  
    
#     return tmp,gate_count





#   netlist=re.sub("assign .* = .*;","",netlist) #replace with rmassign fn

# def archive_extract_gates_v(netlist):
#     netlist=re.sub("module.*;\n?","",netlist)
#     netlist=re.sub("input.*;\n?","",netlist)
#     netlist=re.sub("endmodule\n?","",netlist)
#     netlist=re.sub("assign.*;\n?","",netlist)
#     netlist=re.sub("DFF.*;\n?","",netlist)
    

    
#     netlist=re.sub(r"("+ verilog_gates[2] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",r"\4 = NOT(\2)",netlist)
#     netlist=re.sub(r"("+ verilog_gates[1] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",r"\4 = BUF(\2)",netlist)
#     netlist=re.sub(r"("+ verilog_gates[0] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",r"\4 = BUF(\2)",netlist)

#     for i in verilog_gates[3:]:
#         netlist=re.sub(r"( "+ i +".* \( \.A\()(.*)(\), \.B\()(.*)(\), \.Y\()(.*)(\) \))",r"\6 = "+ re.sub(v_gates_ps,"",i).upper() +r"(\2,\4)",netlist)   
  
#     return netlist




# def extract_gates_v(netlist):
#     # tmp={i:[] for i in verilog_gates}
#     netlist=re.sub(r"("+ verilog_gates[2] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",r"\4 = NOT(\2)",netlist)
#     netlist=re.sub(r"("+ verilog_gates[1] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",r"\4 = BUF(\2)",netlist)
#     netlist=re.sub(r"("+ verilog_gates[0] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",r"\4 = BUF(\2)",netlist)

#     for i in verilog_gates[3:]:
#         netlist=re.sub(r"( "+ i +".* \( \.A\()(.*)(\), \.B\()(.*)(\), \.Y\()(.*)(\) \))",r"\6 = "+ re.sub(v_gates_ps,"",i).upper() +r"(\2,\4)",netlist)   
  
#     return netlist



####################################################################################################################################
####################################################################################################################################
