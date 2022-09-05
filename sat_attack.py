# Import the MonoSAT library
from monosat import *
from utils import *
import subprocess


def updatebit(la0,lb0,o0):
	return Xor(Xnor(la0,o0),la0),Xor(Xnor(lb0,o0,lb0))

def oracle(input="0000000000"):
	return format(subprocess.check_output("/home/alira/FYP/oracle/oracle " + input,shell=True))[2:-1]


bench=open("/home/alira/FYP/tmp/tmp.bench").read()
gates,gate_count = extract_gates_b(bench)
inputs = extract_io_b(bench, mode="input")
outputs = extract_io_b(bench, mode="output")
# print(inputs)



inputvar={i:Var() for i in inputs if("key" not in i)}
keyvarA= {i:Var() for i in inputs if("key" in i)}
keyvarB= {i:Var() for i in inputs if("key" in i)}


def gen_cir(inputvar,keyvar,outputs):
	outputvar={i:Var() for i in outputs}
	wire={}
	ionodes={**inputvar,**keyvar,**outputvar}
	for i in gates:
		tmp = gates[i]
		for j in tmp:
				tmpio=[None]*len(j)
				for n,k in enumerate(j):
					# print(i,k)
					if(k not in ionodes):
						wire[k]=Var()
						tmpio[n]=wire[k]
					else:
						tmpio[n]=ionodes[k]
				
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


def assign_val(binary,keydict):
	for i,x in enumerate(list(keydict.keys())):
		# print(x)
		keydict[x]=True if (binary[i]=='1') else False
	

outputA=gen_cir(inputvar,keyvarA,outputs)
outputB=gen_cir(inputvar,keyvarB,outputs)

out=outputA.keys()
outxor=[]

for i in out:
	outxor.append(Xor(outputA[i],outputB[i]))

# print("THIS",outxor)


constraints=[And(outxor)]

# Assert(And(constraints))



keyvalA,keybinA=randKey(len(keyvarA), seed=10)
keyvalB,keybinB=randKey(len(keyvarB), seed=9)

print("{} {:3} {}".format(len(keyvarA),keyvalA,keybinA))
print("{} {:3} {}".format(len(keyvarB),keyvalB,keybinB))

assign_val(keybinA,keyvarA)
assign_val(keybinB,keyvarB)



# print(keybinA,"  ",keybinB)
print("KEY:  ",dict_to_bin(keyvarA),"  ",dict_to_bin(keyvarB))
inputbin=dict_to_bin(inputvar)
print(inputbin)


tmpac=[]

# Solve()



print("OUT: ",dict_to_bin(outputA)," ",dict_to_bin(outputB))

for i in range(10):
	
	Assert(And(constraints))
	tmps = Monosat().newSolver()
	
	Monosat().setSolver(tmps)
	result=Solve()


	inputbin=dict_to_bin(inputvar)
	inputdict=bin_to_dict(inputvar,inputbin)
	# print(gate_count)
	# print(inputbin)
	# print(len(oracle(inputbin))," ",oracle(inputbin))
	# print(len(dict_to_bin(outputA))," ",dict_to_bin(outputA))
	# outabin=dict_to_bin(outputA)

	# print(bin_to_dict(outputA,oracle(inputbin)))

	o=bin_to_dict(outputA,oracle(inputbin))
	
	cA=gen_cir(inputdict,bin_to_dict(keyvarA,dict_to_bin(keyvarA)),outputs)
	cB=gen_cir(inputdict,bin_to_dict(keyvarB,dict_to_bin(keyvarB)),outputs)



	tmpA=[]
	tmpB=[]
	for i in cA:
		tmpA.append(Xor(Xnor(cA[i],o[i]),outputA[i]))
		tmpB.append(Xor(Xnor(cB[i],o[i]),outputB[i]))


	
	constraints.append(And(tmpA))
	constraints.append(And(tmpB))

		



	# constraints.append()
	# Assert(And(constraints))

	print("KEY:  ",dict_to_bin(keyvarA),"  ",dict_to_bin(keyvarB))
	inputbin=dict_to_bin(inputvar)
	print(inputbin)

	# print(dict_to_bin(outputA))
	# print(dict_to_bin(outputB))
	
	print(dict_to_bin(outputA)," ",dict_to_bin(outputB))

	keyvalA,keybinA=randKey(len(keyvarA), seed=random.random())
	keyvalB,keybinB=randKey(len(keyvarB), seed=random.random())

	print("{} {:3} {}".format(len(keyvarA),keyvalA,keybinA))
	print("{} {:3} {}".format(len(keyvarB),keyvalB,keybinB))


	assign_val(keybinA,keyvarA)
	assign_val(keybinB,keyvarB)

	



result=Solve()

# print(inputvar)
print(dict_to_bin(inputvar))





# tmp=updatebit(False,True,True)
# print(tmp[0])
# for i in keyvarA:
# 	print(type(keyvarA[i]))



#######################################################################################
# for i in inputvar:
# 	print(i," ",inputvar[i].value())

# for i in outputA:
# 	print(i," ",outputA[i].value()," ",outputB[i].value())

# print(outputA)
# print(oracle())