import sys
import re


def getnodeport(buskey):
    inpdict={}
    for i in re.sub(" ","",re.findall(buskey+"(.*);",netlist)[0]).split(","):
        #print(i)
        if(("[" in i) and ("]" in i)):
            tmpis=i.split("[")
            if tmpis[0] in inpdict:
                inpdict[tmpis[0]]+=1
            else:
                inpdict[tmpis[0]]=0 
        elif("[" in i or "]" in i):
            print("ERROR INVALID SYNTAX")
        else:
            inpdict[i]=0  

    print(inpdict)
    
    busnodes=""
    portnodes=""
    for i in inpdict.keys():
        portnodes=portnodes+i+","
        if(inpdict[i]!=0):
            #print("["+str(inpdict[i])+":0] "+i)
            busnodes=busnodes+buskey+" ["+str(inpdict[i])+":0] "+i+"; "
        else:
            #print(i)
            busnodes=busnodes+buskey+" "+i+"; "
    portnodes=portnodes[:-1]
    #print(busnodes,"\n",portnodes)
    return busnodes,portnodes



print("PYTHON SCRIPT START")
if(len(sys.argv)<1):
    print("######################## ERROR ########################")
else:
    netlist=open(sys.argv[1]).read()
    #netlist=open("/home/alira/FYP/btv_output.v").read()

    inputnodes,inputportnodes=getnodeport("input")
    outputnodes,outputportnodes=getnodeport("output")

    # print(inputnodes,"\n",inputportnodes)
    # print(outputnodes,"\n",outputportnodes)


    #print("\n\n",inputportnodes+","+outputportnodes)
    #print("\n\n",inputnodes+"\n "+outputnodes)

    #netlist=re.sub("input .*"+r"ALUCtrl\[0\]"+".*;",inputnodes,netlist)
    netlist=re.sub("input.*;",inputnodes,netlist)
    netlist=re.sub("output.*;",outputnodes,netlist)
    netlist=re.sub("(top.*\()(.*)(\);)",r"\1"+inputportnodes+","+outputportnodes+r"\3",netlist)

    #sys.argv[1]
    with open(sys.argv[1], 'w') as f:
        f.write(netlist)
    print("PYTHON SCRIPT ENDED WITHOUT ERROR")
    
    #\/home/alira/FYP/output

# python3 /home/alira/FYP/python/cleanoutbus.py /home/alira/FYP/btv_output.v

