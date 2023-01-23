# Import the MonoSAT library
from cgi import print_arguments
from unittest import result
from monosat import *
from src.utils import *
from src.netlist import *
import subprocess

import z3 





def oracle(inp):
	if(inp=='000'):
		out='00'
	elif(inp=='001'):
		out='01'
	elif(inp=='010'):
		out='01'
	elif(inp=='011'):
		out='10'
	elif(inp=='100'):
		out='01'
	elif(inp=='101'):
		out='10'
	elif(inp=='110'):
		out='10'
	elif(inp=='111'):
		out='11'
	else:
		return -1
	
	outb=[True if(i=="1") else False for i in out]
	return outb





def gen_cir(inputvar,gates,outputs):
	wire={}
	for i in gates:
		tmp = gates[i]
		for j in tmp:
			for n,k in enumerate(j):
				if(k not in list(inputvar.keys())):
					wire[k]=Var()

	for i in gates:
		for j in tmp:
			# print(j)
			tmpio=[None]*len(j)
			for n,k in enumerate(j):
				if(k not in list(inputvar.keys())):
					tmpio[n]=wire[k]
				else:
					tmpio[n]=inputvar[k]
			
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

	keyvar= {i:wire[i] for i in inputs if("key" in i)}
	outputvar={i:wire[i] for i in outputs}
	return keyvar,outputvar,wire



def gen_dip(inputs,keya,keyb,outputA,outputB,constraints):
	result=Solve(And(constraints))
	if(result):
		return [keya[i].value() for i in keya],[keyb[i].value() for i in keyb],[inputs[i].value() for i in inputs]
		#dict_to_bin(keya),dict_to_bin(keyb),dict_to_bin(inputs),dict_to_bin(outputA),dict_to_bin(outputB)
	else:
		return -1
  

bench=open("/home/alira/FYP/tmp/output_graph.bench").read()
gates,gate_count = extract_gates_b(bench)
inputs = extract_io_b(bench, mode="input")
outputs = extract_io_b(bench, mode="output")
inputvar={i:Var() for i in inputs if("key" not in i)}



class gate:
	def __init__(self,type,output,inputs):
		self.output=output
		self.inputs=inputs
		self.type=type
		
gatecol={}
for i in gates:
	for k in gates[i]:
		# print(i,k)
		gatecol[k[0]]=gate(i,k[0],k[1:])
		

# print(gatecol)
# print([gatecol[i].output for i in gatecol])

# print(inputs)
# print(gates)
# print(outputs)




def get_cir_r():
	keyvar={}
	wirevar={}

	def getr(gate: gate)-> Var:
		inpvar={i:None for i in gate.inputs}
		for i in inpvar:
			if(i in inputs):
				if("key" not in i):
					inpvar[i]=inputvar[i]
				else:
					inpvar[i]=Var()
					keyvar[i]=inpvar[i]
			elif(i in wirevar):	
				inpvar[i]=wirevar[i]
			else:
				# print(i,gatecol[i])
				inpvar[i]=getr(gatecol[i])
				# wirevar[i]=inpvar[i]

		type=gate.type
		# print(type,gate.output,inpvar)
		# print(gate.output)
		if(type=="NOT"):
			result=Not(inpvar[gate.inputs[0]])
		elif(type=="BUF"):
			result=inpvar[gate.inputs[0]]
		elif(type=="AND"):
			result=And(inpvar[gate.inputs[0]],inpvar[gate.inputs[1]])
		elif(type=="OR"):
			result=Or(inpvar[gate.inputs[0]],inpvar[gate.inputs[1]])
		elif(type=="NAND"):
			result=Nand(inpvar[gate.inputs[0]],inpvar[gate.inputs[1]])
		elif(type=="NOR"):
			result=Nor(inpvar[gate.inputs[0]],inpvar[gate.inputs[1]])
		elif(type=="XOR"):
			result=Xor(inpvar[gate.inputs[0]],inpvar[gate.inputs[1]])
		elif(type=="XNOR"):
			result=Xnor(inpvar[gate.inputs[0]],inpvar[gate.inputs[1]])
		else:
			print("GATE NOT FOUND")
			print(i)
			return -1
	
		wirevar[gate.output]=result
		return result
  
	# print(gatecol[i])
	# print(outputs[0])
	# print(getr(gatecol[outputs[0]]))
	# print(outputs[1])
	# print(getr(gatecol[outputs[1]]))

	# {i:getr(gatecol[i]) for i in outputcls}
	
	return {i:getr(gatecol[i]) for i in outputs},keyvar


# get_cir_r()



# outputs.reverse()

# /home/alira/FYP/tmp/output_graph.bench



outputA,keyvarA=get_cir_r()




# print(inputvar)
# print(keyvarA)

node=list(outputA.keys())[0]

print(outputA[node])


result=Solve(Not(outputA[node]))
print(result)

# for i in inputvar:
# 	print(inputvar[i].value())


print(dict_to_bin(inputvar))


# constraints=[And([Xor(outputA[i],outputB[i]) for i in outputA])]
# print(gen_dip(inputvar,keyvarA,keyvarB,outputA,outputB,constraints))

# for i in keyvarA:
# 	print(i,keyvarA[i].value(),keyvarB[i].value())
# # for i in inputvar:
# # 	print(i,inputvar[i].value())

# # print(dict_to_bin(inputvar,printo=True,reverse=False))



# o=oracle(dict_to_bin(inputvar,printo=True,reverse=False))
# print("oracle= ",o)
# o_dict=bin_to_dict(outputA,o)

# # print(o_dict)
# for i in outputA:
# 	print(i,o_dict[i],outputA[i].value(),outputB[i].value())






# tmpo=[Xor(o_dict[i],outputA[i]) for i in outputA]
# constraints.append(And(tmpo))

# tmpo=[Xor(o_dict[i],outputB[i]) for i in outputB]
# constraints.append(And(tmpo))

# # tmpi=[Xor(inputvar[i],inputvar[i].value()) for i in inputvar]
# # constraints.append(And(tmpi))


# print(gen_dip(inputvar,keyvarA,keyvarB,outputA,outputB,constraints))



# print(
#   gen_dip(
#     inputvar,keyvarA,keyvarB,outputA,outputB,
#     [And([Xor(outputA[i],True) for i in outputA])]#,And(constraints[1:])
#     )
# )


# for i in keyvarA:
# 	print(i,keyvarA[i].value(),keyvarB[i].value())







# # t3 = AND(a,b)
# # t4 = XOR(a,b)
# # t5 = OR(t3,t1)
# # t6 = XOR(c,t0)
# # t7 = AND(t0,c)

# # Cout = XnOR(t5,key0)
# # S = XOR(t6,key1)
# # t1 = XOR(t7,key2)
# # t0 = XnOR(t4,key3)



# # _07a_ = NAND(c,a)
# #  _07_ =XOR(_07a_,key0)
# #  _08a_ = OR(c,a)
# #  _08_ =XOR(_08a_,key1)
# #  _09a_ = NAND(_07_,_08_)
# #  _09_ =XOR(_09a_,key2)
# #  _10a_ = NAND(b,_09_)
# #  _10_ =XOR(_10a_,key3)
# #  _05_ = OR(b,_09_)
# #  S = NAND(_10_,_05_)
# #  _06_ = NAND(b,_08_)
# #  Cout = NAND(_07_,_06_)
 
 




# #   INPUT(a)
# #  INPUT(b)
# #  INPUT(c)

# #  INPUT(key0)
# #  INPUT(key1)
# #  INPUT(key2)
# #  INPUT(key3)

# #  OUTPUT(Cout)
# #  OUTPUT(S)

# #  _07a_ = NAND(c,a)
# #  _07_ = XNOR(_07a_,key0)
# #  _08a_ = OR(c,a)
# #  _08_ = XOR(_08a_,key1)
# #  _09a_ = NAND(_07_,_08_)
# #  _09_ = XNOR(_09a_,key2)
# #  _10a_ = AND(b,_09_)
# #  _10_ = XOR(_10a_,key3)
# #  _05_ = OR(b,_09_)
# #  S = NAND(_10_,_05_)
# #  _06_ = NAND(b,_08_)
# #  Cout = NAND(_07_,_06_)
 