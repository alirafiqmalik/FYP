from re import T
from unittest import result
# from monosat import *
from utils import *
from random import randint



def oracle(a,b,c):
	inp=''
	for i in [a,b,c]:
		inp+='1' if(i==True) else '0'

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
	
	outb=[True if(i=="1") else False for i in out]
	return outb

def cir(a,b,c,key):
	t0=Var()
	t1=Var()
	t3=Var()
	Cout=Var()
	S=Var()
	t0=Xor(a,b)
	t1=Xnor(And(t0,c),key[2])
	t3=And(a,b)
	Cout=Xor(Or(t3,t1),key[0])
	S=Xnor(Xor(c,t0),key[1])
	return Cout,S


def intarray(n=3):
	tmp=randint(0,7)
	tmp=format(tmp,'0'+'3'+'b')
	return [True if i=='1' else False for i in tmp] 



a=Var()
b=Var()
c=Var()

keya=[Var(),Var(),Var()]
keyb=[Var(),Var(),Var()]

Ca,Sa=cir(a,b,c,keya)#[False,True,True]
Cb,Sb=cir(a,b,c,keyb)

# Solve(And((Ca),Not(Sa)))

# print(a.value(),b.value(),c.value())
# # print([i.value() for i in keya])


# print(Ca.value(),Sa.value())

# o=oracle(a.value(),b.value(),c.value())
# print(o)


cons_C=[Ca,Cb]
cons_S=[Sa,Sb]

constraints=[]


def get_dip(a,b,c,keya,keyb,Ca,Cb,Sa,Sb,constraints):
	result=Solve(And(constraints))

	pass

for i in range(10): #64

	result=Solve(And(constraints))
	print("SAT",result)
	if(result==False):
		break

	# print(a.value(),b.value(),c.value())
	print([i.value() for i in keya])
	print([i.value() for i in keyb])
	o=oracle(a.value(),b.value(),c.value())

	tmpa=Var(symbol=a.value())
	tmpb=Var(symbol=b.value())
	tmpc=Var(symbol=c.value())
	cCa,cSa=Var(symbol=Ca.value()),Var(symbol=Sa.value())
	cCb,cSb=Var(symbol=Cb.value()),Var(symbol=Sb.value())

	# cCa,cSa=cir(tmpa,tmpb,tmpc,[i.value() for i in keya]) #[i.value() for i in keya]
	# cCb,cSb=cir(tmpa,tmpb,tmpc,[i.value() for i in keyb]) #[i.value() for i in keyb]
	# print(tmpa,tmpb,tmpc)

	print("INP= ",a.value(),b.value(),c.value())
	print(Ca.value(),Sa.value())
	print(Cb.value(),Sb.value())
	print(cCa)
	# constraints=[Xor(cons_C),Xor(cons_S)]
	constraints.append(And(Xor(a,tmpa),Xor(b,tmpb),Xor(c,tmpc)))
	# constraints.append(And(Xor(cCa,Ca),Xor(cCb,Cb),Xor(cSa,Sa),Xor(cSb,Sb)))
	Monosat().newSolver()

	keya=[Var(),Var(),Var()]
	keyb=[Var(),Var(),Var()]

	a=Var()
	b=Var()
	c=Var()
	

	Ca,Sa=cir(a,b,c,keya)#[False,True,True]
	Cb,Sb=cir(a,b,c,keyb)
	cons_C=[Ca,Cb]
	cons_S=[Sa,Sb]


	# constraints.append(Xnor(cCa,o[0]))
	# constraints.append(Xnor(cSa,o[1]))
	# constraints.append(Xnor(cCb,o[0]))
	# constraints.append(Xnor(cSb,o[1]))

	# print("ORACLE: ",o)




result=Solve(And(constraints))
print("SAT",result)
print("INP= ",a.value(),b.value(),c.value())
print(Ca.value(),Sa.value())
print(Cb.value(),Sb.value())




# cons_C.append(Xnor(Ca,o[0]))
# cons_C.append(Xnor(Cb,o[0]))
# cons_S.append(Xnor(Sa,o[1]))
# cons_S.append(Xnor(Sb,o[1]))

# constraints.append(Xor(Xnor(cCa,o[0]),Ca))
# constraints.append(Xor(Xnor(cSa,o[1]),Sa))
# constraints.append(Xor(Xnor(cCb,o[0]),Cb))
# constraints.append(Xor(Xnor(cSb,o[1]),Sb))


#   # Assert(And(constraints))
  

# # Assert(And([Xnor(Ca,Cb),Xnor(Sa,Sb)]))
# # Assert(Sa)

# print(i)
# # And(Equal(Ca,Cb),Equal(Sa,Sb))
# result=Solve()
# print(result)

# print(a.value(),b.value(),c.value())




# print([i.value() for i in keya])
# print([i.value() for i in keya])

# o=oracle(a.value(),b.value(),c.value())

# print(o)
# print(Ca.value(),Sa.value())
# print(Cb.value(),Sb.value())