import re

#gates=['INVX1', 'AND2X1', 'OR2X1', 'NAND2X1', 'NOR2X1']
#gates=['not_g', 'and_g', 'or_g', 'nand_g', 'nor_g']
#gates=['NOT', 'AND', 'OR', 'NAND', 'NOR']
gates=['BUFF','BUF','NOT_g', 'AND_g', 'OR_g', 'NAND_g', 'NOR_g','XOR_g','XNOR_g']
flipflops=['DFFcell', 'DFFSRcell']

netlist=open('/home/alira/FYP/tmprtl.v').read()
# /home/alira/FYP/linux/final.v
# /home/alira/FYP/output.v

netlist=re.sub("//.*\n","",netlist)
netlist=re.sub("[/][*].*[*][/]","",netlist)
netlist=re.sub("[(][*].*[*][)]\n","",netlist)

netlist=re.sub("wire .*;\n","",netlist)

#print(re.findall("assign (.*) = .*;",netlist))

# for i in re.findall("assign (.*) = .*;",netlist):
#     print(i)
# netlist=re.sub("assign .* = .*;","",netlist)
# print(re.findall("assign .* = .*;",netlist))



netlist=re.sub("\n","",netlist)
netlist=re.sub("\s+"," ",netlist)
netlist=re.sub(";",";\n",netlist)
netlist=re.sub("endmodule","endmodule\n",netlist)

# for i in re.findall("assign (.*) = .*;",netlist):
#     print(i,re.findall(i,netlist))
#     print(re.findall("wire .*"+i+" ;",netlist))

#print(re.findall("assign (.*) = .*;",netlist))


# with open('/home/alira/FYP/output.v', 'w') as f:
#     f.write(netlist)




netlist=re.sub(r"("+ gates[2] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",r"\4 = NOT(\2)",netlist)
netlist=re.sub(r"("+ gates[1] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",r"\4 = BUF(\2)",netlist)
netlist=re.sub(r"("+ gates[0] +".* \( \.A\()(.*)(\), \.Y\()(.*)(\) \))",r"\4 = BUF(\2)",netlist)

for i in gates[3:]:
    #print(i)
    netlist=re.sub(r"( "+ i +".* \( \.A\()(.*)(\), \.B\()(.*)(\), \.Y\()(.*)(\) \))",r"\6 = "+ re.sub("_g","",i).upper() +r"(\2,\4)",netlist)



for i in re.findall("input .*;\n",netlist):
    if("[" in i):
        tmpstr=""
        tmp=re.findall("input \[(\d+):(\d+)\] (.*);",i)[0]
        for k in range(int(tmp[1]),int(tmp[0])+1):
            tmpstr=tmpstr+"INPUT("+tmp[2]+"["+str(k)+"]);"+"\n"
           # print("INPUT("+tmp[2]+"["+str(k)+"])")

    else: 
        tmp=i.split(" ")[-1][:-2]
        tmpstr="INPUT("+tmp+");"
        #print(tmp)
        #print("INPUT("+tmp+")")
    
    tmpi=re.sub("\[","\[",i)
    tmpi=re.sub("\]","\]",tmpi)
    #print(tmpi)
 
    netlist=re.sub(tmpi,tmpstr,netlist)
    #print(tmpstr,end="\n <----------------------->  \n")
    #print(i)

for i in re.findall("output .*;\n",netlist):
    if("[" in i):
        tmpstr=""
        tmp=re.findall("output \[(\d+):(\d+)\] (.*);",i)[0]
        for k in range(int(tmp[1]),int(tmp[0])+1):
            tmpstr=tmpstr+"OUTPUT("+tmp[2]+"["+str(k)+"]);"+"\n"
            #print("OUTPUT("+tmp[2]+"["+str(k)+"])")
    else: 
        tmp=i.split(" ")[-1][:-2]
        tmpstr="OUTPUT("+tmp+");"+"\n"
        #print(tmp)
        #print("OUTPUT("+tmp+")")
    #print(tmpstr,end="\n <----------------------->  \n")
    tmpi=re.sub("\[","\[",i)
    tmpi=re.sub("\]","\]",tmpi)
    #print(tmpi)
    netlist=re.sub(tmpi,tmpstr,netlist)
    #print(i)   


for i in re.findall(flipflops[0]+" .* \( .C\((.*)\), .D\((.*)\), .Q\((.*)\) \)",netlist):
    print(i)



netlist=re.sub(";\n ",";\n",netlist)
netlist=re.sub("(module top.*;\n)",r"# \1",netlist)
netlist=re.sub("endmodule","",netlist)
netlist=re.sub("\s+"," ",netlist)
netlist=re.sub("\n","",netlist)
netlist=re.sub(";","\n",netlist)
#netlist=re.sub(";\n ",";\n",netlist)





with open('/home/alira/FYP/tmp/hb.py', 'w') as f:
    f.write(netlist)









#for i in netlist.split(";"):
#    print(i)
#    break




#template=open("/home/alira/FYP/yosys/manual/PRESENTATION_Intro/mycells.v").read()
#re.findall("module (.*)[(]",template)

#with open('./python/template.txt', 'w') as f:
#    f.write(template)


#for j in re.findall(r"("+ i +".* \( \.A\()(.*)(\), \.B\()(.*)(\), \.Y\()(.*)(\) \))",netlist)[0]:
#        print(j,end="    <------->    ")
#    break
