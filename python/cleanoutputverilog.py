import sys
import re
from benchtograph import getnodeport




print("PYTHON SCRIPT START")
if(len(sys.argv)<2):
    print("######################## ERROR ########################")
    raise Exception("NO ARGUMEMTS PASSED")
else:
    netlist=open(sys.argv[1]).read()
    if(len(sys.argv)==3):
        netlist=re.sub(sys.argv[2],r"top",netlist)
        print("DID")
    
    
    netlist=re.sub("\n","",netlist)
    netlist=re.sub("\s+"," ",netlist)
    netlist=re.sub(";",";\n",netlist)

    netlist=re.sub("module\s?(.*)\s?\(\s?",r"\nmodule \1(",netlist)

    netlist=re.sub("[/][*].*[*][/]","",netlist)
    netlist=re.sub(r"//.*\n","",netlist)
    netlist=re.sub(r"\\","",netlist)

    if(len(sys.argv)==3):
        inputportnodes,inputnodes=getnodeport(netlist,"input")
        outputportnodes,outputnodes=getnodeport(netlist,"output")
        netlist=re.sub("input .*;",inputnodes,netlist)
        netlist=re.sub("output .*;",outputnodes,netlist)
        netlist=re.sub("(top.*\()(.*)(\);)",r"\1"+inputportnodes+","+outputportnodes+r"\3",netlist)


    
    netlist=re.sub("\n","",netlist)
    netlist=re.sub("\s+"," ",netlist)
    netlist=re.sub(";",";\n",netlist)


    with open(sys.argv[1], 'w') as f:
        f.write(netlist)
    print("PYTHON SCRIPT ENDED WITHOUT ERROR")
#\/home/alira/FYP/output