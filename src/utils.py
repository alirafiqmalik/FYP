import re
import random

#gates=['INVX1', 'AND2X1', 'OR2X1', 'NAND2X1', 'NOR2X1']
#gates=['not_g', 'and_g', 'or_g', 'nand_g', 'nor_g']
#gates=['NOT', 'AND', 'OR', 'NAND', 'NOR']
v_gates_ps="_g"
verilog_gates=['BUF_g','NOT_g', 'AND_g', 'OR_g', 'NAND_g', 'NOR_g','XOR_g','XNOR_g']
bench_gates=['DFF','BUF','NOT', 'AND', 'OR', 'NAND', 'NOR','XOR','XNOR']




####################################################################################################################################
####################################################################################################################################
def text_to_pattern(text):
  text=re.sub(r"\\",r"\\\\",text)

  text=re.sub(r"\[",r"\[",text)
  text=re.sub(r"\]",r"\]",text)

  text=re.sub(r"\{",r"\{",text)
  text=re.sub(r"\}",r"\}",text)
  
  # text=re.sub("","",text)
  return text


####################################################################################################################################
####################################################################################################################################

def gen_busport(node,size:int):
    port=""
    if(type(node)==str):
        for i in range(size):
            port+=node+format(str(size-i-1),"")+", "
        port=port[:-2]
    return port

####################################################################################################################################
####################################################################################################################################


def get_diference(a,b):
    tmpa=list(set(a) - set(b))
    tmpb=list(set(b) - set(a))
    tmplist=[tmpa,tmpb]#list(set(tmpa)|set(tmpb))
    return tmplist

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

    portnodes, busnodes,_ = io_port(tmpval[0].split(", "), mode=buskey)
    # print(io_port(tmpval[0].split(", ")))
    return portnodes, busnodes


####################################################################################################################################
####################################################################################################################################

def io_port(inputs, mode="input"):
    tmpdict = {}
    replace_=[]
    for i in inputs:
        # if(re.findall("(.*)_(\d+)_?",i)!=[]):
        #     i=re.sub("(.*)_(\d+)_?",r"\1"+"["+r"\2"+"]",i)
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
            replace_.append(i)
        else:
            # replace_.remove(i)
            inputnodes = inputnodes+mode+" "+i+"; "

    # inputnodes=inputnodes[:]
    portnodes = portnodes[:-1]
    return portnodes, inputnodes,replace_

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

def randKey(bits, seed=None):
    if(seed!=None):
        random.seed(seed)
    intkey = random.randint(0, (2**bits)-1)
    tmpkey = format(intkey, "0"+str(bits)+"b")
    return intkey, tmpkey

####################################################################################################################################
####################################################################################################################################


"module antisat_{name} (A,B,Q);parameter keyval = {key},n={ic}; input [n-1:0] A; input [2n-1:0] B; output Q;always @ (A or B) begin  if (B == keyval) begin    Q = 1;  end else begin    Q = 0;end end endmodule"
"module antisat_{name} (A,KEY,Q);parameter n={ic}; input [n-1:0] A; input [2n-1:0] B; output Q;always @ (A or B) begin  if (B == {keyval}) begin    Q = 1;  end else begin    Q = 0;end end endmodule"

"module antisat_{name} (A,KEY,Q);parameter n={ic};input [n-1:0] A; input [2n-1:0] KEY; output Q; wire Q1,Q2; g_block g(A,KEY[n-1:0],Q1); g_block gc(A,KEY[2n-1:n],Q2); assign Q = Q1 & Q2;endmodule \nmodule g_block(X,KEY_X,Q);parameter n={ic};input [n-1:0]X;input [n-1:0]KEY_X;output reg Q;wire [n-1:0]X_xor;assign X_xor=X^KEY_X;integer k;always@(*)begin Q=1;for(k=0;k<n-1;k=k+1)begin if(X_xor[k]==0) Q=0;end end endmodule"

def gencc_AntiSAT(modulename, inputs):
    codestr="module {name} (A,KEY,Q);parameter n={ic};input [n-1:0] A; input [2*n-1:0] KEY; output Q; wire Q1,Q2; g_block g(A,KEY[n-1:0],Q1); g_block gc(A,KEY[2*n-1:n],Q2); assign Q = Q1 & (~Q2);endmodule \n\nmodule g_block(X,KEY_X,Q);parameter n={ic};input [n-1:0]X;input [n-1:0]KEY_X;output reg Q;wire [n-1:0]X_xor;assign X_xor=X^KEY_X;integer k;always@(*)begin Q=1;for(k=0;k<n-1;k=k+1)begin if(X_xor[k]==0) Q=0;end end endmodule"
    ic = len(inputs)
    portnodes, _,_ = io_port(inputs)
    
    comver = codestr.format(name=modulename,ic=ic)
    port=modulename+" {init} ("+"{portnodes},"+"{KEY}"+",{Q}); "

    return re.sub(";", ";\n", comver), portnodes,port


####################################################################################################################################
####################################################################################################################################

def gencc(modulename, inputs, key):
    ic = len(inputs)
    portnodes, inputnodes,_ = io_port(inputs)
    if (key == None):
        comver = "module "+modulename+"("+portnodes+",KEY,Q); " + inputnodes + "input ["+str(ic-1)+":0]KEY;" + " wire ["+str(
            ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; always@(*)begin if(A==KEY)Q=1;else Q=0;end endmodule"
        port=modulename+" {init} ("+portnodes+",{key},{Q}); "
    else:
        comver = "module "+modulename+"("+portnodes+",Q); " + inputnodes + " wire ["+str(
            ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; always@(*)begin if(A=="+str(ic)+"'d"+str(key)+")Q=1;else Q=0;end endmodule"
        port=modulename+" {init} ("+portnodes+",{Q}); "

    return re.sub(";", ";\n", comver), portnodes,port


####################################################################################################################################
####################################################################################################################################


def hammingcc(modulename, inputs, h, key=None):
    ic = len(inputs)
    portnodes, inputnodes,_ = io_port(inputs)
    # print("HERE ",io_port(inputs))
    if (key == None):
        comver = "module "+modulename+"("+portnodes+",KEY,Q); " + inputnodes + "input ["+str(ic-1)+":0]KEY; wire ["+str(
            ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; integer Qr,count,i; always@(*)begin Qr=KEY^A;count=0; for(i=0;i<"+str(ic)+";i=i+1)begin if(Qr[i]) count=count+1;end if(count=="+str(h)+")Q=1;else Q=0; end endmodule"
        port=modulename+" {init} ("+portnodes+",{key},{Q}); "
    else:
        comver = "module "+modulename+"("+portnodes+",Q); " + inputnodes + " wire ["+str(ic-1)+":0]A; assign A={"+portnodes+"}; output reg Q; integer Qr,count,i; always@(*)begin Qr="+str(
            ic)+"'d"+str(key)+"^A;count=0; for(i=0;i<"+str(ic)+";i=i+1)begin if(Qr[i]) count=count+1;end if(count=="+str(h)+")Q=1;else Q=0; end endmodule"
        port=modulename+" {init} ("+portnodes+",{Q}); "
    return re.sub(";", ";\n", comver), portnodes,port




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
  netlist=re.sub("end ","end\n",netlist)
  netlist=re.sub("begin","begin\n",netlist)
  return netlist

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################


def format_bench(netlist):
#   netlist=re.sub("//.*\n","",netlist)
#   netlist=re.sub("[/][*].*[*][/]","",netlist)
#   netlist=re.sub("#.*\n","\n",netlist)
  netlist=re.sub("#.*\n","\n",netlist)
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
        if(i.lower() in bench):
            ix=i.lower()
        else:
            ix=i

        if i=='NOT' or i=='BUF' or i=='DFF':
            tmp[i]=re.findall(" ?(.*) = "+ ix +"\((.*)\)\n?",bench)

            i.lower()
        else:
            tmp[i]=re.findall(" ?(.*) = "+ ix +"\((.*), ?(.*)\)\n?",bench)
        
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


# def extract_io_v(verilog,mode="input"):
#     tmp=re.findall(mode.lower()+" (.*);",verilog)
#     for i in tmp:
#         tmpi=i.split(",")
#         print(tmpi)


# def getio_v(verilog,mode="input"):
#   tmp=re.findall(mode.lower()+" (.*);",verilog)
#   tmp=tmp[0].split(",")
# #   print(tmp[0].split(","))
#   #if("," in i) 
#   port=""
#   nodes=[]
#   for ii in tmp:
#     i=ii.strip()
#     if(("[" in i) and ("]" in i)):
#       tmpi=re.findall("(.*)\[(.*):(.*)]",i)[0]
#       port+=tmpi[0]+","
#       for j in range(int(tmpi[2]),int(tmpi[1])+1):
#         # print(tmpi[0]+"["+str(j)+"]")
#         nodes.append(tmpi[0]+"["+str(j)+"]")
#     else:
#       port+=i+","
#       nodes.append(i)
# #   print(nodes)
#   return nodes,port



####################################################################################################################################
####################################################################################################################################


def extract_gates_va(verilog):
  tmp={}
  gate_count = {}
  tmp["BUF"]=re.findall("assign (.*) = (.*) ?;",verilog)
  tmp["NOT"]=re.findall("assign (.*) = ~(.*) ?;",verilog)
  tmp["AND"]=re.findall("assign (.*) = (.*) & (.*) ?;",verilog)
  tmp["OR"]=re.findall("assign (.*) = (.*) | (.*) ?;",verilog)
  tmp["XOR"]=re.findall("assign (.*) = (.*) ^ (.*) ?;",verilog)
  
  for i in tmp.keys():
    if(tmp[i]!=[]):    
        gate_count[i] = len(tmp[i])
  return tmp,gate_count


####################################################################################################################################
####################################################################################################################################


def extract_io_v(verilog,mode="input"):
  nodes=[]
  port=""
  tmp=re.findall(mode.lower()+" (.*);",verilog)
  for i in tmp:
    if("[" in i):
      ei,si,tmpi=re.findall(r"\[(\d+)\:(\d+)\] (.*)",i)[0]
      port+=tmpi+","
      for i in range(int(si),int(ei)+1):
        nodes.append(tmpi+"["+str(i)+"]")
    elif("," in i):
        tmpi=i.split(",")
        nodes=merge_lists((nodes,tmpi))

    else:
      nodes.append(i)
      port+=i+","
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
        tmpx=re.findall(" ?"+verilog_gates[1] + r" .* \( .A\((.*)\), .Y\((.*)\) \) ?;",verilog)
    elif(i=="BUF_g"):
        tmpx=re.findall(" ?"+verilog_gates[0] +r" .* \( .A\((.*)\), .Y\((.*)\) \) ?;",verilog)
    else:
        tmpx=re.findall(" ?"+i +r" .* \( .A\((.*)\), .B\((.*)\), .Y\((.*)\) \) ?;",verilog)

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
