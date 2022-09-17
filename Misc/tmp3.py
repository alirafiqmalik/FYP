from re import T
from unittest import result
from monosat import *
from src.utils import *
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
	key0,key1,key2,key3=key

	Cout=Var()
	S=Var()

	_07_ = Nand(c,a)
	_08_ = Or(c,a)
	_09_ = Nand(_07_,_08_)
	_10_ = Nand(b,_09_)
	_05a_ = Or(b,_09_)
	_05_ = Xnor(key3,_05a_)
	_01a_ = Nand(_10_,_05_)
	_06a_ = Nand(b,_08_)
	_06_ = Xor(key0,_06a_)
	_00a_ = Nand(_07_,_06_)
	
	Cout = Xnor(key1,_00a_)
	S = Xor(key2,_01a_)
	
	
		
	return Cout,S


def intarray(n=3):
	tmp=randint(0,7)
	tmp=format(tmp,'0'+'3'+'b')
	return [True if i=='1' else False for i in tmp] 


def get_dip(a,b,c,keya,keyb,Ca,Cb,Sa,Sb,constraints):
	result=Solve(And(constraints))
	if(result):
		return ([i.value() for i in keya],[i.value() for i in keyb]),(a.value(),b.value(),c.value()),(Ca.value(),Sa.value()),(Cb.value(),Sb.value())
	else:
		return -1



a=Var()
b=Var()
c=Var()

keya=[Var(),Var(),Var(),Var()]
keyb=[Var(),Var(),Var(),Var()]

Ca,Sa=cir(a,b,c,keya)
Cb,Sb=cir(a,b,c,keyb)



# print([(keya[i],keyb[i]) for i,_ in enumerate(keya)])

# ,And([Xor(keya[i],keyb[i]) for i,_ in enumerate(keya)])
constraints=[And(Xor(Ca,Cb),Xor(Sa,Sb))]

for i in range(10):
	tmp=get_dip(a,b,c,keya,keyb,Ca,Cb,Sa,Sb,constraints)
	print(tmp)
	if(tmp==-1):
		print(get_dip(a,b,c,keya,keyb,Ca,Cb,Sa,Sb,And([Xnor(Ca,Cb),Xnor(Sa,Sb)])))
		o=oracle(a.value(),b.value(),c.value())
		print([i.value() for i in keya])
		print("ORACLE-1: ",o)
		break
	else:
		o=oracle(a.value(),b.value(),c.value())
		print("ORACLE: ",o)
		cCb,cSb=o[0],o[1]
		
		# constraints.append(And(Xor(cCb,Ca),Xor(cCb,Cb),Xor(cSb,Sa),Xor(cSb,Sb)))
		constraints.append(And(Xor(cCb,Ca),Xor(cCb,Cb)))
		constraints.append(And(Xor(cSb,Sa),Xor(cSb,Sb)))
		# constraints.append(And(Xor(cCb,Ca,Cb),Xor(cSb,Sa,Sb)))
		tmpa,tmpb,tmpc=a.value(),b.value(),c.value()
		constraints.append(And(Xor(a,tmpa),Xor(b,tmpb),Xor(c,tmpc)))
		print([i.value() for i in keya])

		# if((cCb!=Ca.value())or (cSb!=Sa.value())):
		# 	print("A")
		# 	tmpk=[i.value() for i in keya]
		# 	# constraints.append(And(Xor(keya[0],tmpk[0]),Xor(keya[1],tmpk[1]),Xor(keya[2],tmpk[2])))
		# 	# constraints.append(And(Xor(keyb[0],tmpk[0]),Xor(keyb[1],tmpk[1]),Xor(keyb[2],tmpk[2])))
		# if((cCb!=Cb.value())or (cSb!=Sb.value())):
		# 	print("B")
		# 	tmpk=[i.value() for i in keyb]
			# constraints.append(And(Xor(keya[0],tmpk[0]),Xor(keya[1],tmpk[1]),Xor(keya[2],tmpk[2])))
			# constraints.append(And(Xor(keyb[0],tmpk[0]),Xor(keyb[1],tmpk[1]),Xor(keyb[2],tmpk[2])))


# o=oracle(a.value(),b.value(),c.value())
# print(o)

# cCb,cSb=o[0],o[1]
# constraints.append(And(Xor(cCb,Ca),Xor(cCb,Cb),Xor(cSb,Sa),Xor(cSb,Sb)))

# tmpa,tmpb,tmpc=True, True, True
# constraints.append(And(Xor(a,tmpa),Xor(b,tmpb),Xor(c,tmpc)))


# print(get_dip(a,b,c,keya,keyb,Ca,Cb,Sa,Sb,constraints))

# print(get_dip(a,b,c,keya,keyb,Ca,Cb,Sa,Sb,[Xnor(Ca,Cb),Xnor(Sa,Sb)]))

