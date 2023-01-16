from random import randint
import re
import src.utils as utils


verilog=open("/home/alira/FYP/linux/assign_tech.v").read()


t,c=utils.extract_gates_v(verilog)
print(c)
# print(t)

# s="{gate} .* ( .A({A}), .B({B}), .Y({Y}) );"
si=" {} (.*) \( .A\({}\), .B\({}\), .Y\({}\) \);"
s=" {} .* \( .A\({}\), .B\({}\), .Y\({}\) \);"
l="{} keygateinit{count} ( .A(keyinput{count}), .B({}), .Y({}) );"
v="{} {} ( .A({}), .B({}), .Y({}) );"

kgate=["XOR_g","XNOR_g"]

keyvalue=101
bits=8
keybit = format(keyvalue, "0"+str(bits)+"b")

print(keybit)
keygatecount=0



print(randint(0,10))

# print(t)

j=0

while(1):
  for i in t:
    # print("H ",keygatecount,bits-keygatecount)
    biti=int(keybit[bits-keygatecount-1])
    
    ti=t[i][j]
    
    tx=si.format(i+"_g",ti[0],ti[1],ti[2])
    ts=s.format(i+"_g",ti[0],ti[1],ti[2])
    tl=l.format(" "+kgate[int(keybit[biti])],ti[2],ti[2]+"key",count=str(keygatecount))
    
    init=re.findall(tx,verilog)
    if(init!=[]):
      init=re.findall(tx,verilog)[0]
      newstr=v.format(" "+i+"_g",init,ti[0],ti[1],ti[2]+"key")+"\n"+tl
      verilog=re.sub(ts,newstr,verilog)

    # print(ts)
    # print("------------------")
    # print(newstr)
    # print("###########")
      keygatecount+=1
    if(bits==keygatecount):
      break





with open("/home/alira/FYP/tmptop.v","w") as f:
  f.write(verilog)





# keynodes=utils.gen_busport("keyinput",10)
# print(keynodes)



# "NAND_g _1377_ ( .A(_0043_), .B(_0225_), .Y(_0226_) );\n XOR_g keygate{i} ( .A(_0226_), .B(keygate{i}), .Y(_0226_) );"










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



# verilog=open("/home/alira/FYP/linux/assign_tech.v").read()


# tmp=re.findall("input"+" (.*);",verilog)

# for i in tmp:
#   if("," in i):
#     print(i)
#   elif("[" in i and "]" in i and "," in i):
#     print("++> ",i)
#   elif("[" in i and "]" in i):
#     print("==> ",i)
#   else:
#     print("-->",i)






# from src.LL import PostSAT_LL
# LL=PostSAT_LL(b,mode="verilog")
# lockcir=LL.SFLL()

# with open("/home/alira/FYP/tmptop.v","w") as f:
#   f.write(lockcir)