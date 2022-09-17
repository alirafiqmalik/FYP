#  python3 sat_attack/sat_attack/run.py /home/alira/FYP/linux/sat_attack/benchmarks/sample/sample_locked.v /home/alira/FYP/linux/sat_attack/benchmarks/sample/sample_unlocked.v


# Import the MonoSAT library
from monosat import *
from src.utils import *
import subprocess



def oracle(input="00000000000000000000000000000000000000000"):
	return format(subprocess.check_output("/home/alira/FYP/oracle/oracle " + input,shell=True))[2:-1]

	


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


def assign_val(binary,keydict):
	for i,x in enumerate(list(keydict.keys())):
		# print(x)
		keydict[x]=True if (binary[i]=='1') else False
	

# bench=open("/home/alira/FYP/tmp/tmp.bench").read()
bench=open("/home/alira/FYP/tmp/tmp_yosys.bench").read()
gates,gate_count = extract_gates_b(bench)
inputs = extract_io_b(bench, mode="input")
outputs = extract_io_b(bench, mode="output")
# print(inputs)


def gen_dip(inputs,keya,keyb,outputA,outputB,constraints):
	result=Solve(And(constraints))
	if(result):
		return dict_to_bin(keya),dict_to_bin(keyb),dict_to_bin(inputs),dict_to_bin(outputA),dict_to_bin(outputB)
	else:
		return -1


inputvar={i:Var() for i in inputs if("key" not in i)}
# keyvarA= {i:Var() for i in inputs if("key" in i)}
# keyvarB= {i:Var() for i in inputs if("key" in i)}

# outputA=gen_cir(inputvar,keyvarA,gates,outputs)
# outputB=gen_cir(inputvar,keyvarB,gates,outputs)

binary="10100"
inpkey=[i for i in inputs if("key" in i)]
keyvarA= {i:Var(symbol=True if (binary[n]=='1') else False) for n,i in enumerate(inpkey)}

# print(keyvarA)
outputA=gen_cir(inputvar,keyvarA,gates,outputs)

inp="00010000000000000000000000000000000000010"
# inp_dict=bin_to_dict(inputvar,inp)
o=oracle(inp)
print(o)
out_dict=bin_to_dict(outputA,o)

# for i in outputA:
# 	print(i,out_dict[i],outputA[i])
# 	# And(out_dict[i],outputA[i])


r=Solve(And([Xnor(Var(symbol=out_dict[i]),outputA[i]) for i in outputA]))
# print([And(outputA[i],out_dict[i]) for i in outputA])

print(dict_to_bin(outputA))


print(dict_to_bin(inputvar))
print(inp)

# print(oracle(inp))


# assign_val("",keyvarA)










# constraints=[Xor(outputA[i],outputB[i]) for i in outputA]

# print(gen_dip(inputvar,keyvarA,keyvarB,outputA,outputB,constraints))


# print(dict_to_bin(inputvar))

# print(dict_to_bin(outputA))
# print(dict_to_bin(outputB))

# o=oracle(dict_to_bin(inputvar))
# print("oracle= ",o)


# o_dict=bin_to_dict(outputA,o)

# tmpo=[And(Xor(o_dict[i],outputA[i]),Xor(o_dict[i],outputB[i])) for i in outputA]
# constraints.append(And(tmpo))
# tmpi=[Xor(inputvar[i],inputvar[i].value()) for i in inputvar]
# constraints.append(And(tmpi))


# print("___________________________________")

# print(gen_dip(inputvar,keyvarA,keyvarB,outputA,outputB,constraints))

# print(
# 	gen_dip(inputvar,keyvarA,keyvarB,outputA,outputB,[Xnor([Xnor(outputA[i],outputB[i]) for i in outputA])])
# 	)

# [Xnor([Xnor(outputA[i],outputB[i]) for i in outputA]),Xnor([Xnor(keyvarA[i],keyvarB[i]) for i in keyvarA])]



















# print(dict_to_bin(inputvar))
# print(dict_to_bin(outputA))
# print(dict_to_bin(outputB))
# o=oracle(dict_to_bin(inputvar))
# print("oracle= ",o)


# ka,kb,=gen_dip(inputvar,keyvarA,keyvarB,constraints)
# o=oracle(dict_to_bin(inputvar))
# print(dict_to_bin(ka))
# print(dict_to_bin(kb))

# print(dict_to_bin(inputvar))

# print(dict_to_bin(outputA))
# print(dict_to_bin(outputB))

# print(o)



# o=oracle(a.value(),b.value(),c.value())
# print(o)
# cCb,cSb=o[0],o[1]
# constraints.append(And(Xor(cCb,Ca),Xor(cCb,Cb),Xor(cSb,Sa),Xor(cSb,Sb)))
# tmpa,tmpb,tmpc=a.value(),b.value(),c.value()
# constraints.append(And(Xor(a,tmpa),Xor(b,tmpb),Xor(c,tmpc)))














# out=outputA.keys()
# outxor=[]

# for i in out:
# 	outxor.append(Xor(outputA[i],outputB[i]))

# # print("THIS",outxor)


# constraints=[And(outxor)]

# # Assert(And(constraints))



# keyvalA,keybinA=randKey(len(keyvarA), seed=10)
# keyvalB,keybinB=randKey(len(keyvarB), seed=9)

# print("{} {:3} {}".format(len(keyvarA),keyvalA,keybinA))
# print("{} {:3} {}".format(len(keyvarB),keyvalB,keybinB))

# assign_val(keybinA,keyvarA)
# assign_val(keybinB,keyvarB)



# # print(keybinA,"  ",keybinB)
# print("KEY:  ",dict_to_bin(keyvarA),"  ",dict_to_bin(keyvarB))
# inputbin=dict_to_bin(inputvar)
# print(inputbin)


# tmpac=[]

# # Solve()



# print("OUT: ",dict_to_bin(outputA)," ",dict_to_bin(outputB))

# for i in range(10):
	
# 	Assert(And(constraints))
# 	tmps = Monosat().newSolver()
	
# 	Monosat().setSolver(tmps)
# 	result=Solve()


# 	inputbin=dict_to_bin(inputvar)
# 	inputdict=bin_to_dict(inputvar,inputbin)
# 	# print(gate_count)
# 	# print(inputbin)
# 	# print(len(oracle(inputbin))," ",oracle(inputbin))
# 	# print(len(dict_to_bin(outputA))," ",dict_to_bin(outputA))
# 	# outabin=dict_to_bin(outputA)

# 	# print(bin_to_dict(outputA,oracle(inputbin)))

# 	o=bin_to_dict(outputA,oracle(inputbin))
	
# 	cA=gen_cir(inputdict,bin_to_dict(keyvarA,dict_to_bin(keyvarA)),outputs)
# 	cB=gen_cir(inputdict,bin_to_dict(keyvarB,dict_to_bin(keyvarB)),outputs)



# 	tmpA=[]
# 	tmpB=[]
# 	for i in cA:
# 		tmpA.append(Xor(Xnor(cA[i],o[i]),outputA[i]))
# 		tmpB.append(Xor(Xnor(cB[i],o[i]),outputB[i]))


	
# 	constraints.append(And(tmpA))
# 	constraints.append(And(tmpB))

		



# 	# constraints.append()
# 	# Assert(And(constraints))

# 	print("KEY:  ",dict_to_bin(keyvarA),"  ",dict_to_bin(keyvarB))
# 	inputbin=dict_to_bin(inputvar)
# 	print(inputbin)

# 	# print(dict_to_bin(outputA))
# 	# print(dict_to_bin(outputB))
	
# 	print(dict_to_bin(outputA)," ",dict_to_bin(outputB))

# 	keyvalA,keybinA=randKey(len(keyvarA), seed=random.random())
# 	keyvalB,keybinB=randKey(len(keyvarB), seed=random.random())

# 	print("{} {:3} {}".format(len(keyvarA),keyvalA,keybinA))
# 	print("{} {:3} {}".format(len(keyvarB),keyvalB,keybinB))


# 	assign_val(keybinA,keyvarA)
# 	assign_val(keybinB,keyvarB)

	



# result=Solve()

# # print(inputvar)
# print(dict_to_bin(inputvar))





# # tmp=updatebit(False,True,True)
# # print(tmp[0])
# # for i in keyvarA:
# # 	print(type(keyvarA[i]))



# #######################################################################################
# # for i in inputvar:
# # 	print(i," ",inputvar[i].value())

# # for i in outputA:
# # 	print(i," ",outputA[i].value()," ",outputB[i].value())

# # print(outputA)
# # print(oracle())