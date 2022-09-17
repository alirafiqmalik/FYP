import circuit
import tokenizer
import node
import parser
from src.utils import *
from node import Node


def read_nodes(filename,file_type="v"):
  verilog=open(filename).read()
  if(file_type=='v'):
    inp,_=getio_v(verilog,'input')
    out,_=getio_v(verilog,'output')
    gates,_=extract_gates_v(verilog)
  elif(file_type=='b'):
    inp= extract_io_b(verilog,mode='input')
    out=extract_io_b(verilog,mode='output')
    gates,_=extract_gates_b(verilog)
  else:
    print("ERROR")


  node={}
  for i in inp:
    # print(i,[],"Primary Input","Key Input")
    if('key' in i):
      node[i]=Node(i,[],"Key Input")
      # print(node[i])
    else:
      node[i]=Node(i,[],"Primary Input")
      # print(node[i])


  for i in gates:
    for j in gates[i]:
      # print(i.title(),j[-1],list(j[:-1]))
      # pass
      node[j[-1]]=Node(j[-1],list(j[:-1]),i.title())
  
  return  node,out




def read_nodes2(filename):
    """
    Reads in the nodes of a circuit from a benchmakr file.
    filename: the name of the benchmark file
    returns: the nodes of the circuit, the output names of the circuit
    """
    with open(filename) as f:
        t = tokenizer.Tokenizer(f)
        p = parser.Parser()
        nodes, output_names = p.parse(t)
        # print("HERE ",nodes, output_names)
        return nodes, output_names



def read_ckt(filename):
    """
    Reads in a circuit from a benchmark file.
    filename: the name of the benchmark file
    returns: object representation of the circuit
    """
    nodes, output_names = read_nodes(filename)
    return circuit.Circuit.from_nodes(nodes, output_names)



if __name__ == "__main__":
  locked_filename2="/home/alira/FYP/obf.v"
  locked_filename="/home/alira/FYP/tmprtl.v"


  tmp=read_nodes("/home/alira/FYP/linux/CSAW/ASSURE_LOCKED/design1/oracle1.bench",file_type='b')
  # tmp2=read_nodes2(locked_filename2)


  print(tmp[0])
  # print("\n\n")
  # print(tmp2)
  

  # print(type(tmp[1]),type(tmp[0]))
  # print(tmp[1])
  # for i in tmp[0]:
  #   print(i,tmp[0][i],type(tmp[0][i]))
  #   print("THIS = ",i,"-",tmp[0][i].name,"-",tmp[0][i].inputs,"-",tmp[0][i].type)#type(tmp[0][i].name),tmp[0][i].z3_repr)
  #   break

  
  # lockedopen=format_verilog(open("/home/alira/FYP/tmprtl.v").read())
  
  # inp=extract_io_v(lockedopen,mode="input")
  # out=extract_io_v(lockedopen,mode="output")
  # gates,_=extract_gates_v(lockedopen)
  
  # print(gates)
  # for i in gates:
  #   print(i)

  # node.Node(name, inputs, type)

# export PYTHONPATH="/home/alira/FYP:$PYTHONPATH"