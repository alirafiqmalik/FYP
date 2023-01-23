from src.utils import extract_gates_b,extract_io_b
from z3 import *



def Nor(*args):
  return Not(Or(args))

def Nand(*args):
  return Not(And(args))

def Xnor(*args):
  return Not(Xor(args))


def gen_cir(inputvar,keyvar,gates,outputs):
	outputvar={i:Var() for i in outputs}
	wire={}
	ionodes={**inputvar,**keyvar,**outputvar}
	# print(gates["AND"])
	# print("########################################################################################\n\n\n")
	for i in gates:
		tmp = gates[i]
		# print(tmp)
		# print("###########",i," ====> ",tmp,"###########\n\n\n")
		for j in tmp:
				# print(j)
				tmpio=[None]*len(j)
				for n,k in enumerate(j):
					# print(i,k)
					if((k not in ionodes) and (k not in wire)):
						wire[k]=Var()
						tmpio[n]=wire[k]
					elif (k in wire):
						tmpio[n]=wire[k]
					else:
						tmpio[n]=ionodes[k]
				
				# print(j,tmpio)
				if(i=="NOT"):
					tmpio[0]=Not(tmpio[1])
				elif(i=="BUF"):
					tmpio[0]=tmpio[1]
				elif(i=="AND"):
					tmpio[0]=And(tmpio[1],tmpio[2])
				elif(i=="OR"):
					tmpio[0]=Or(tmpio[1],tmpio[2])
				elif(i=="NAND"):
					tmpio[0]=Nand(tmpio[1],tmpio[2])
				elif(i=="NOR"):
					tmpio[0]=Nor(tmpio[1],tmpio[2])
				elif(i=="XOR"):
					tmpio[0]=Xor(tmpio[1],tmpio[2])
				elif(i=="XNOR"):
					tmpio[0]=Xnor(tmpio[1],tmpio[2])
				else:
					print("GATE NOT FOUND")
					print(i)
	return outputvar



bench=open("/home/alira/FYP/org.bench").read()
print(extract_gates_b(bench)[0].keys())


gates,gate_count = extract_gates_b(bench)
inputs = extract_io_b(bench, mode="input")
outputs = extract_io_b(bench, mode="output")

inputvar={i:Var() for i in inputs if("key" not in i)}


binary="10100"
inpkey=[i for i in inputs if("key" in i)]
keyvar= {i:Var(symbol=True if (binary[n]=='1') else False) for n,i in enumerate(inpkey)}

outputA,keyvarA=gen_cir(inputvar,keyvar,gates,outputs)




# s = Solver()
# s.add(And(Not(Y),X))
# print(s.check())

# print(s.model())