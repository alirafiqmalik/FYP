from src.netlist import *
import subprocess
from src.utils import sortio, randKey, gencc, hammingcc,format_verilog, io_port
from src.cmds import *

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################


class LogicLocking(Netlist):
    def __init__(self, netlist: str) -> None:
        super().__init__(netlist)
        self.keygates = {'XOR': 0, 'XNOR': 0}
        self.keygatescount = 0
        self.FSgates = {'XOR': 0, 'XNOR': 0}
        self.FSgatescount = 0
        self.FRgates = {'XOR': 0, 'XNOR': 0}
        self.FRgatescount = 0
        self.FSinputs = []
        self.FRinputs = []

    def keynodes(self) -> dict:
        return self.keygates

    def FSnodes(self) -> dict:
        return self.FSgates

    def FRnodes(self) -> dict:
        return self.FRgates

    def InsertFSGate(self, NodeA: str, NodeB: str, gatetype: str = 'XOR',) -> None:
        FSgatescount = self.gates[gatetype]
        FSgate = gatetype+"_"+str(FSgatescount)

        FRgatescount = FSgatescount+1
        FRgate = gatetype+"_"+str(FRgatescount)

        self.circuitgraph.remove_edge(NodeA, NodeB)

        keywireS = "FSwire"+str(self.FSgatescount)
        keywireR = "FRwire"+str(self.FRgatescount)

        self.circuitgraph.add_edge(NodeA, keywireS)
        self.circuitgraph.add_edge(keywireS, FSgate)
        self.circuitgraph.add_edge(FSgate, keywireR)

        self.circuitgraph.add_edge(keywireR, FRgate)

        self.circuitgraph.add_edge(FRgate, NodeB)

        self.circuitgraph.add_edge("FSI_"+str(self.FSgatescount), FSgate)
        self.circuitgraph.add_edge("FRI_"+str(self.FRgatescount), FRgate)

        self.FSinputs.append("FSI_"+str(self.FSgatescount))
        self.FRinputs.append("FRI_"+str(self.FRgatescount))

        self.wires.append(keywireS)
        self.wires.append(keywireR)

        self.gates[gatetype] += 2
        self.gatecount += 2

        self.FSgates[gatetype] += 1
        self.FSgatescount += 1

        self.FRgates[gatetype] += 1
        self.FRgatescount += 1

    def InsertKeyGate(self, NodeA: str, NodeB: str, gatetype: str = 'XOR') -> None:
        keygatecount = self.gates[gatetype]
        keygate = gatetype+"_"+str(keygatecount)

        self.circuitgraph.remove_edge(NodeA, NodeB)

        # keywire = "KEY"+str(len(self.wires))
        keywire = "keywire"+str(len(self.wires))

        self.circuitgraph.add_edge(NodeA, keywire)
        self.circuitgraph.add_edge(keywire, keygate)
        self.circuitgraph.add_edge(keygate, NodeB)

        # self.circuitgraph.add_edge("KEY["+str(self.keygatescount)+"]", keygate)
        # self.inputs.append("KEY["+str(self.keygatescount)+"]")

        self.circuitgraph.add_edge("keyinput_"+str(self.keygatescount), keygate)
        self.inputs.append("keyinput_"+str(self.keygatescount))

        self.wires.append(keywire)

        self.gates[gatetype] += 1
        self.gatecount += 1

        self.keygates[gatetype] += 1
        self.keygatescount += 1

    def RLL(self, n: int, key: int) -> list:
        bitkey = format(key, "b")
        print(2**n, "<----->", key, "<----->", (2**n) >= key)
        if (n > len(bitkey)):
            bitkey = format(key, "0"+str(n)+"b")
        elif (n < len(bitkey)):
            print("ERROR")
            print("Number of Gates < Number of Key-Bits")
            return None
        # else:
        print("n == Bits")

        print("######################################", end="\n          ")
        print(key, " ----------> ", bitkey)
        print("######################################")

        random.seed(10)
        for i in range(n):
            tp = random.randint(0, len(self.wires)-1)
            inp = list(self.circuitgraph.predecessors(self.wires[tp]))
            if (bitkey[-(i+1)] == '1'):
                self.InsertKeyGate(inp[0], self.wires[tp], 'XNOR')
            else:
                self.InsertKeyGate(inp[0], self.wires[tp], 'XOR')
        
    def SLL(self, n: int, key: int) -> list:
        bitkey = format(key, "b")
        print(2**n, "<----->", key, "<----->", (2**n) >= key)
        if (n > len(bitkey)):
            bitkey = format(key, "0"+str(n)+"b")
        elif (n < len(bitkey)):
            print("ERROR")
            print("Number of Gates < Number of Key-Bits")
            return None
        # else:
        print("n == Bits")

        print("######################################", end="\n          ")
        print(key, " ----------> ", bitkey)
        print("######################################")

        random.seed(10)
        for i in range(n):
            tp = random.randint(0, len(self.wires)-1)
            inp = list(self.circuitgraph.predecessors(self.wires[tp]))
            if (bitkey[-(i+1)] == '1'):
                self.InsertKeyGate(inp[0], self.wires[tp], 'XNOR')
            else:
                self.InsertKeyGate(inp[0], self.wires[tp], 'XOR')

    def FindConeinputs(self, node):
        if node in self.inputs:
            return [node]
        # elif (node in [circuit.FFnodes()]):
        else:
            coneinputnode = []
            pred = self.circuitgraph.predecessors(node)
            for i in pred:
                coneinputnode = list(set(coneinputnode) |
                                     set(self.FindConeinputs(i)))
            return coneinputnode

    def MaxInputCone(self):
        maxcount = 0
        maxtmp = []
        maxout = ""
        for i in self.outputs:
            tmp = self.FindConeinputs((i))
            if (len(tmp) > maxcount):
                maxcount = len(tmp)
                maxtmp = tmp
                maxout = i
        return maxtmp, maxout

    def getCRunits(self, key=None, HD=0):  # 734
        # tmp,outnode=circuit.MaxInputCone()
        tmp = self.inputs
        sortio(tmp)
        if (key == None):
            key, tmpkey = randKey(len(tmp))
            print(len(tmp), " ===>> ", len(tmpkey),
                  " ===>> ", key, " ===>> ", tmpkey, "\n")

        # cc= hammingcc("corrupt",tmp,HD,key)
        # rsc=hammingcc("restore",tmp,HD,None)
        cc = gencc("corrupt", tmp, key)
        rsc = gencc("restore", tmp, None)
        return cc, rsc

    def SFLLHD(self, outputpath="./output.v", HD=None, key=None):  # 734
        cctxt, rstx = self.getCRunits(key=key, HD=HD)
        inpnodes = self.inputs
        sortio(inpnodes)
        outnodes = self.outputs
        for coneout in outnodes:
            coneinp = self.FindConeinputs(coneout)
            sortio(coneinp)
            # if(tmp==coneinp):
            tmpi = list(self.circuitgraph.predecessors(coneout))[0]
            self.InsertFSGate(tmpi, coneout)

        keyi = ["keyinput"+i for i in inpnodes]
        sortkey = io_port(keyi)

        self.graph_to_bench("./tmp/output_graph.bench")

        subprocess.run(cmd2.format("./tmp/output_graph.bench",
                       "./tmp/btv_output_graph.v"), shell=True)

        
        # subprocess.run(
        #     "python3 /home/alira/FYP/python/cleanoutputverilog.py /home/alira/FYP/btv_output_graph.v \/home/alira/FYP/output", shell=True)

        # format_verilog()

        # netlist=re.sub(sys.argv[2],r"top",netlist)
        netlist = open("./tmp/btv_output_graph.v").read()
        netlist = format_verilog(netlist)
        print( "HERE",re.findall("module .* ?\((.*)\) ?;", netlist))
        netlist = re.sub("module .* ?\((.*)\) ?;",
                         r"module top (\1) ;", netlist)
        
        with open("./tmp/btv_output_graph.v", 'w') as f:
            f.write(netlist)

        tmpx = "corrupt C" + "("+cctxt[1]+","+"FSO"+");\nrestore R" + \
            "("+rstx[1]+",{"+sortkey[0]+"},FRO"+");\n"

        for i in range(self.FSnodes()["XOR"]):
            tmpss = "FSI_"+str(i)
            tmpsr = "FRI_"+str(i)

            tmpx += "assign FSI_"+str(i)+"=FSO;\n"
            tmpx += "assign FRI_"+str(i)+"=FRO;\n"

            netlist = re.sub("input .*"+tmpss+".*;", "", netlist)
            netlist = re.sub(tmpss+" ?,", "", netlist)

            netlist = re.sub("input.*"+tmpsr+".*;", "", netlist)
            netlist = re.sub(tmpsr+" ?,", "", netlist)

        tmpx += "endmodule\n"

        netlist = re.sub("(module .*\(.*)(\);)", r"\1," +
                         sortkey[0]+");"+sortkey[1], netlist)

        netlist = re.sub("\s+", " ", netlist)
        netlist = re.sub(";", ";\n", netlist)

        netlist = re.sub("endmodule", tmpx, netlist)
        netlist += "\n\n"+cctxt[0]
        netlist += "\n\n"+rstx[0]

        with open("./tmp/tmp_input.v", 'w') as f:
            f.write(netlist)

        subprocess.run(cmd1.format(inputfile="./tmp/tmp_input.v",rtlv= "./tmp/tmpoutput.v",
                       outputfile=outputpath,cppfile="", getcpp="", gettmpv=""), shell=True)
        # print("###################################################\nDONE")
        
        # subprocess.run(
        #     "python3 /home/alira/FYP/python/misc_vtb_obs.py", shell=True)

        # subprocess.run("python3 /home/alira/FYP/python/cleanoutputverilog.py "+outputpath,shell=True)

    def graph_to_bench(self, outpath: str) -> None:
        graphtonetlist = ""
        for i in self.inputs:
            graphtonetlist += "INPUT("+i+")"+"\n"
            # print("INPUT("+i+")")

        for i in self.FSinputs:
            graphtonetlist += "INPUT("+i+")"+"\n"

        for i in self.FRinputs:
            graphtonetlist += "INPUT("+i+")"+"\n"

        for i in self.outputs:
            # print("OUPUT("+i+")")
            graphtonetlist += "OUTPUT("+i+")"+"\n"
        for i in self.gatenodes().keys():
            for j in range(self.gatenodes()[i]):
                tmpj = i+"_"+str(j)
                inp = list(self.circuitgraph.predecessors(tmpj))
                out = list(self.circuitgraph.successors(tmpj))
                if (i == "NOT" or i == 'BUF'):
                    graphtonetlist += out[0]+" = "+i+"("+inp[0]+")"+"\n"
                else:
                    graphtonetlist += out[0]+" = "+i + \
                        "("+inp[0]+","+inp[1]+")"+"\n"
        print("Writing BENCH File to Location: ", outpath)
        with open(outpath, 'w') as f:
            f.write(graphtonetlist)


####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
