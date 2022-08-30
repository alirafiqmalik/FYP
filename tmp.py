from monosat import *
from utils import *

def oracle(a,b,c):
	if({a,b,c}=={True,False,False}):
		False
	elif({a,b,c}=={False,True,False}):
		False
	elif({a,b,c}=={False,False,True}):
		False
	elif({a,b,c}=={True,False,False}):
		False
	elif({a,b,c}=={False,False,False}):
		False
	else:
		return True

def cir(a0,a1,a2,key0,key1,key2):
	t0=Var()
	t1=Var()
	t2=Var()
	t3=Var()
	t4=Var()
	t5=Var()
	t6=Var()

	t7=Var()

	o=Var()


	t0=Nand(a0,a1)
	t1=Nand(a1,a2)
	t2=Nand(a2,a0)

	t3=Xnor(key0,t0)
	t4=Xnor(key1,t1)
	t5=Xor(key2,t2)

	t6=Nand(t4,t5)

	t7=t6

	o=Or(t3,t7)

	# Assert(o)

	return o



a0 = Var()
a1 = Var()
a2 = Var()



ao=cir(a0,a1,a2,True,True,False)
bo=cir(a0,a1,a2,True,True,True)


Assert(Xor(ao,bo))


tmp=[a0,a1,a2]


result = Solve()  # Solve the instance in MonoSAT, return either True if the instance is SAT, and False if it is UNSAT
if result:
	print("SAT")
	# print(str(t1.value())+" "+str(t0.value()))
	print(str(ao.value()))
	print(str(bo.value()))
	print("Oracle=",oracle(ao,a1,a2))
	for i in tmp:
		print(str(i.value()),end=" ")
	print()
else:
	print("UNSAT")
 
#  not keys
# True,True,False  
ao=cir(a0,a1,a2,False,True,False)
bo=cir(a0,a1,a2,True,True,True)


Assert(Xor(Xor(Xnor(ao,oracle(ao,a1,a2)),ao),Xor(Xnor(bo,oracle(ao,a1,a2),bo))))



