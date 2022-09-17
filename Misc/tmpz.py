from z3 import *

# from tmpx import gen_cir


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



def is_atom(t):
    if not is_bool(t):
        return False
    if not is_app(t):
        return False
    k = t.decl().kind()
    if k == Z3_OP_AND or k == Z3_OP_OR or k == Z3_OP_IMPLIES:
        return False
    if k == Z3_OP_EQ and t.arg(0).is_bool():
        return False
    if k == Z3_OP_TRUE or k == Z3_OP_FALSE or k == Z3_OP_XOR or k == Z3_OP_NOT:
        return False
    return True

def atoms(fml):
    visited = set([])
    atms = set([])
    def atoms_rec(t, visited, atms):
        if t in visited:
            return
        visited |= { t }
        if is_atom(t):
            atms |= { t }
        for s in t.children():
            atoms_rec(s, visited, atms)
    atoms_rec(fml, visited, atms)
    return atms

def atom2literal(m, a):
    if is_true(m.eval(a)):
        return a
    return Not(a)

# Extract subset of atoms used to satisfy the negation
# of a formula.
# snot is a solver for Not(fml)
# s    is a solver for fml
# m    is a model for Not(fml)
# evaluate each atom in fml using m and create
# literals corresponding to the sign of the evaluation.
# If the model evaluates atoms to false, the literal is
# negated.
# 
#
def implicant(atoms, s, snot):
    m = snot.model()
    lits = [atom2literal(m, a) for a in atoms]
    is_sat = s.check(lits)
    assert is_sat == unsat
    core = s.unsat_core()
    return Or([mk_not(c) for c in core])

#
# Extract a CNF representation of fml
# The procedure uses two solvers
# Enumerate models for Not(fml)
# Use the enumerated model to identify literals
# that imply Not(fml)
# The CNF of fml is a conjunction of the
# negation of these literals.
#

def to_cnf(fml):
    atms = atoms(fml)
    s = Solver()
    snot = Solver()
    snot.add(Not(fml))
    s.add(fml)

    while sat == snot.check():
        clause = implicant(atms, s, snot)
        yield clause
        snot.add(clause)

        
# a, b, c, = Bools('a b c')
# fml = And(And(a,c),And(a,b)) #Or(And(a, b), And(Not(a), c))

# # for clause in to_cnf(fml):
# #     print(clause)

# s = Solver()
# s.add(fml)

# print(s.check())
# print(a.num_args(),b.num_args(),c.num_args())


def Nand(*args):
  return Not(And(args))

def Nor(*args):
  return Not(Or(args))

def Xnor(a,b):
  return Not(Xor(a,b))


def cir(a,b,c,key):
	key0,key1,key2,key3=key

	# Cout=Var()
	# S=Var()

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


# p = Bool('pqr')
# x = Bool('x')
# v = Bool('v')
# solve(Nand(x,p,v))

a,b,c,=Bools('a b c')
keya=Bools('key0a key1a key2a key3a')
keyb=Bools('key0b key1b key2b key3b')

Ca,Sa=cir(a,b,c,keya)
Cb,Sb=cir(a,b,c,keyb)


# print(Ca)
# print(Sa)

constraints=[Xor(Ca,Cb),Xor(Sa,Sb)]

# for i in constraints:
#     print("####################################")
#     print(i)

tmpconA=[None for i in range(10)]
tmpconB=[None for i in range(10)]
tmporc=[None for i in range(10)]

for j in range(1):
    s = Solver()
    s.add(constraints)
    print(s.check())
    if(str(s.check())=="unsat"):
        break
    # print(s.model())

    bin=""
    val=list(s.model())
    val.reverse()
    tmpd={}
    for i in val:
        if('key' not in str(i)):
            # print(i,s.model()[i])
            tmpd[str(i)]=bool(s.model()[i])
            bin+="1" if s.model()[i] else "0"
        elif('key' in str(i)):
            pass
            # print(i,s.model()[i])


    print(bin)
    m = s.model()

    # print(m.evaluate(Ca),m.evaluate(Sa))
    # print(m.evaluate(Cb),m.evaluate(Sb))

    tmporc[j]=oracle(bin)
    # cCac,cSac
    tmpconA[j]=cir(tmpd["a"],tmpd["b"],tmpd["c"],keya)
    tmpconB[j]=cir(tmpd["a"],tmpd["b"],tmpd["c"],keyb)
    
    # print(cCb,cSb)

    # constraints.append(And(Xor(a,tmpd["a"]),Xor(b,tmpd["b"]),Xor(c,tmpd["c"])))

    # print([s.model()[i] for i in list(s.model()) if (("a" in str(i)) and ("key" in str(i)))])
    # print([s.model()[i] for i in list(s.model()) if (("b" in str(i)) and ("key" in str(i)))])

    constraints.append(Xor(Xnor(tmporc[j][0],tmpconA[j][0]),Ca))
    constraints.append(Xor(Xnor(tmporc[j][0],tmpconB[j][0]),Cb))

    constraints.append(Xor(Xnor(tmporc[j][1],tmpconA[j][1]),Sa))
    constraints.append(Xor(Xnor(tmporc[j][1],tmpconB[j][1]),Sb))

    # for i in constraints[2:]:
    #     print("####################################")
    #     print(i)








s = Solver()

# for i in constraints:
#     print("####################################")
#     print(i)


newconst=constraints[1:]
newconst.append(Xnor(Sa,Sb))
newconst.append(Xnor(Ca,Cb))

print(newconst)
s.add(newconst)#constraints[1:])
print(s.check())


# https://github.com/lnestor/sat_attack.git

# # [Xnor(Ca,Cb),Xnor(Sa,Sb)]

bin=""
val=list(s.model())
val.reverse()
tmpd={}
for i in val:
    if('key' not in str(i)):
        # print(i,s.model()[i])
        tmpd[str(i)]=bool(s.model()[i])
        bin+="1" if s.model()[i] else "0"
    elif(('key' in str(i))and ('a' in str(i))):
        print(i,s.model()[i])

print(bin)







# s = Solver()
# s.add(constraints)
# print(s.check())






# bin=""
# val=list(s.model())
# val.reverse()
# tmpd={}
# for i in val:
#   if('key' not in str(i)):
#     print(i,s.model()[i])
#     tmpd[str(i)]=s.model()[i]
#     bin+="1" if s.model()[i] else "0"


# print(bin)
# m = s.model()

# print(m.evaluate(Ca),m.evaluate(Sa))
# print(m.evaluate(Cb),m.evaluate(Sb))




# cCb,cSb=oracle(bin)
# cCac2,cSac2=cir(tmpd["a"],tmpd["b"],tmpd["c"],keya)
# cCbc2,cSbc2=cir(tmpd["a"],tmpd["b"],tmpd["c"],keyb)
# print(cCb,cSb)

# constraints.append(Xor(Xnor(cCb,cCac2),Ca))
# constraints.append(Xor(Xnor(cCb,cCbc2),Cb))



# s = Solver()
# # s.set(Ca)
# s.add(constraints)
# print(s.check())














####################################################################################################################################################################
####################################################################################################################################################################


# s = Solver()
# s.set(Ca)
# s.add([Xnor(Ca,True),Xnor(Sa,True)])
# print(s.check())


# val=list(s.model())
# # val.reverse()
# for i in val:
#   if(("key" in str(i)) and ("a" in str(i))):
#     print(i,s.model()[i])

# inp=[str(i):s.model()[i] for i in list(s.model()) if('key' not in str(i))]
# print(inp)
