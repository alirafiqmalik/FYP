import circuit
from src.utils import extract_io_v,extract_gates_v,extract_io_b,extract_gates_b,format_verilog
from node import Node,DFF



def read_nodes_v(filename):
  verilog=open(filename).read()
  verilog=format_verilog(verilog)
  inp,_=extract_io_v(verilog,'input')
  out,_=extract_io_v(verilog,'output')
  gates,_=extract_gates_v(verilog)

   
  node={}
  for i in inp:
    # print(i)
    if('key' in i):
      node[i]=Node(i,[],"Key Input")
    else:
      node[i]=Node(i,[],"Primary Input")

  # print(gates["BUF"])
  for i in gates:
    for j in gates[i]:
      # print("HERE ",i.title(),j[-1],list(j[:-1]))
      # print(j[-1])
      # if(i=="BUF"):

      tmpj=list(j[:-1])
      # title=i.title()
      # if("1'h0" in j[:-1]):
      #   print("HERE = ",j[-1],j[:-1],type(j[:-1]),i.title())
      #   xji = j[:-1].index("1'h0")
      #   tmpj = tmpj[:xji]+[False]+tmpj[xji+1:]
      #   print(tmpj,type(i.title))
      #   # title=+="_True"
      # elif("1'h1" in j[:-1]):
      #   print("HERE = ",j[-1],j[:-1],type(j[:-1]),i)
      #   xji = j[:-1].index("1'h1")
      #   tmpj = tmpj[:xji]+[True]+tmpj[xji+1:]
      #   print(tmpj)
      
      node[j[-1]]=Node(j[-1],tmpj,i.title())

  # print(out)
  return node,out




def read_nodes_b(filename):
  netlist=open(filename).read()  
  inp= extract_io_b(netlist,mode='input')
  out=extract_io_b(netlist,mode='output')
  gates,_=extract_gates_b(netlist)



  node={}

  for i in inp:
    # print(i,[],"Primary Input","Key Input")
    if('key' in i):
      node[i]=Node(i,[],"Key Input")
    # elif (('clk' in i.lower()) |('clock' in i.lower())):
    #   node["clk"]=Node(i,[],"Key Input")
    # elif (('rst' in i.lower()) |('reset' in i.lower())):
    #   node["rst"]=Node(i,[],"Key Input")
    else:
      node[i]=Node(i,[],"Primary Input")

  for i in gates:
    # print(i)
    for j in gates[i]:
      # print(i.title(),j[-1],list(j[:-1]))
      # if(i=="DFF"):
      #   break
      #   if("clk" not in node):
      #     print(i,"######################################## DFF ERROR NO CLK #####################################")
      #   if("rst" not in node):
      #     print(i,"######################################## DFF ERROR NO RST #####################################")
      # else:
      node[j[0]]=Node(j[0],list(j[1:]),i.title())
  # print("T", node)
  return node,out





def read_ckt(filename,file_type):
    """
    Reads in a circuit from a benchmark file.
    filename: the name of the benchmark file
    returns: object representation of the circuit
    """
    if(file_type=='b'):
       nodes, output_names = read_nodes_b(filename)
    elif(file_type=='v'):
      nodes, output_names = read_nodes_v(filename)
    else:
      Exception("ERROR")
      return None

    # print("H ",nodes)
    # print("There  ",nodes['a'],type(nodes['a']))
    return circuit.Circuit.from_nodes(nodes, output_names)








# def read_nodes2(filename):
#     """
#     Reads in the nodes of a circuit from a benchmakr file.
#     filename: the name of the benchmark file
#     returns: the nodes of the circuit, the output names of the circuit
#     """
#     with open(filename) as f:
#         t = tokenizer.Tokenizer(f)
#         p = parser.Parser()
#         nodes, output_names = p.parse(t)
#         # print("HERE ",nodes, output_names)
#         # print("There  ",nodes['a'],type(nodes['a']))
#         return nodes, output_names


# def get_expected_key(filename):
#     key = {}

#     with open(filename) as f:
#         for line in f.readlines():
#             if "KeyGate" in line:
#                 tokens = line.split()

#                 key_name = tokens[2][0:-1]
#                 key_bit = tokens[0] == "xnor"

#                 if "NOT" in tokens[1]:
#                     key_bit = not key_bit

#                 key[key_name] = key_bit                
#     print("exp = ",key)
#     return key
