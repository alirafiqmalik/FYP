# Import the MonoSAT library
from monosat import *
from utils import *



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
outxor=[None]*len(out)

for i in out:
	outxor=Xor(outputA[i],outputB[i])

Assert(And(outxor))


# for i in keyvarA:
# 	print(i)

keyvalA,keybinA=randKey(len(keyvarA), seed=10)
keyvalB,keybinB=randKey(len(keyvarB), seed=9)

print("{} {:3} {}".format(len(keyvarA),keyvalA,keybinA))
print("{} {:3} {}".format(len(keyvarB),keyvalB,keybinB))



assign_val(keybinA,keyvarA)
assign_val(keybinB,keyvarB)



print(gate_count)


print(Solve())

# for i in out:
# 	print(i," ",outputA[i].value()," ",outputB[i].value())

for i in inputvar:
	print(i," ",inputvar[i].value())
