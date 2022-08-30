import subprocess
from benchtograph import *

# /home/alira/FYP/tmp/tmp.v

# cmd1.format("/home/alira/FYP/btv_org.v","","/home/alira/FYP/btv_org_yosys.v",getcpp="",gettmpv="")
####################################################################################################################
####################################################################################################################
def readtopv():
    netlist=open("/home/alira/FYP/top.v").read()
    with open("/home/alira/FYP/input.v", 'w') as f:
        f.write(netlist)
    subprocess.run(cmd1.format("input.v","./tmpoutput.v","./output.v",getcpp="",gettmpv=""),shell=True)
    subprocess.run("python3 /home/alira/FYP/python/misc_vtb_obs.py",shell=True)
    netlist=open("/home/alira/FYP/netlist.bench").read()
    return netlist
####################################################################################################################
####################################################################################################################
def readbench():
    netlist=open("/home/alira/FYP/input.bench").read()
    org=Netlist(netlist)
    org.graph_to_bench("./org.bench")
    subprocess.run(cmd2.format("/home/alira/FYP/org.bench","/home/alira/FYP/btv_org.v"),shell=True)
    subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/btv_org.v \/home/alira/FYP/org",shell=True)
    subprocess.run(cmd1.format("/home/alira/FYP/btv_org.v","","/home/alira/FYP/btv_org_yosys.v",getcpp="#",gettmpv="#"),shell=True)
    subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/btv_org_yosys.v ",shell=True)
    del org
    return netlist
####################################################################################################################
####################################################################################################################


subprocess.run("clear",shell=True)
netlist=readbench()
# netlist=readtopv()

# circuit=LogicLocking(netlist)
# graph=circuit.graph()
# circuit.gatenodes()
# wires=circuit.wirenodes()
# circuit.info()


# circuit.SFLLHD(outputpath="./output.v",HD=0,key=734)#734
##############################################################################3



######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################













# netlist=re.sub("endmodule","compcir corrupt" +"("+cctxt[1]+","+"FSO"+");\ncompcir restore" +"("+cctxt[1]+","+"FRO"+");\nendmodule",netlist)
# netlist+="\n\n\n"+cctxt[0]

# "compcir corrupt" +"("+cctxt[1]+","+"FSO"+");\ncompcir restore" +"("+cctxt[1]+","+"FRO"+");\nendmodule"

# print("compcir("+cctxt[1]+","+tmpss+");\nendmodule")

# netlist=re.sub("endmodule","compcir "+ "C0" +"("+cctxt[1]+","+tmpss+");\nendmodule",netlist)
# netlist+="\n\n\n"+cctxt[0]

# # btv_output
# with open("/home/alira/FYP/input.v", 'w') as f:
#     f.write(netlist)



# subprocess.run(cmd1.format("input.v","./tmpoutput.v","./output.v",getcpp="",gettmpv=""),shell=True)
# print("###################################################\nDONE")
# subprocess.run("python3 /home/alira/FYP/python/misc_vtb_obs.py",shell=True)





# subprocess.run(cmd1.format("/home/alira/FYP/btv_output.v","/home/alira/FYP/btv_tmpoutput_yosys.v","/home/alira/FYP/btv_output_yosys.v",getcpp="#",gettmpv="#"),shell=True)
# subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/btv_output_yosys.v",shell=True)


# netlist=open("/home/alira/FYP/output.v").read()


# maxcone=circuit.MaxInputCone()
# print(len(maxcone[0]),maxcone[1])
# tmpi=re.sub("\]","\]",re.sub("\[","\[",maxcone[1]))

# print(re.findall(tmpi,netlist))


# circuit.RLL(n=3,key=3)
# print("##################################################")
# circuit.info()

# circuit.graph_to_bench("./output.bench")

#netlist=open("/home/alira/FYP/output.v").read()
# with open("/home/alira/FYP/tmp.v", 'w') as f:
#     f.write(netlist)




########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################
########################################################################################################################################


# def get_ccrs(circuit):
#     tmp=circuit.inputnodes()
#     sortio(tmp)
#     # print(tmp)
#     # tmpval,tmpkey=randKey(len(tmp))
#     # print(len(tmp),len(tmpkey),tmpval,tmpkey,"\n"
#     tmpkey="1011011110"
#     tmpval=int(tmpkey,2)
#     cctxt=gencc("corrupt",tmp,len(tmp),tmpval)
#     rstx=gencc("restore",tmp,len(tmp),None)

#     inpnodes=circuit.inputnodes()
#     sortio(inpnodes)
#     outnodes=circuit.outputnodes()
#     for coneout in outnodes:
#         coneinp=circuit.FindConeinputs(coneout)
#         sortio(coneinp)
#         # if(tmp==coneinp):
#         tmpi=list(graph.predecessors(coneout))[0]
#         circuit.InsertFSGate(tmpi,coneout)


#     inpnodes=circuit.inputnodes()
#     sortio(inpnodes)
#     keyi=["keyinput"+i for i in inpnodes]
#     sortkey=io_port(keyi)

#     circuit.graph_to_bench("/home/alira/FYP/output.bench")



