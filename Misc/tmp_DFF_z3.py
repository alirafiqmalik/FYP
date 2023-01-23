from src.utils import *
import re
from  z3 import *



def Nor(*args):
  return Not(Or(args))


def latch(D,E):
  # D=Var()
  # E=Var()

  X,Y=Bools('X Y')

  Dn=Not(D)

  A=And(Dn,E)
  B=And(D,E)


  X=Nor(X,A)
  Y=Nor(Y,B)

  return X,Y



D,E=Bools('D E')
E=True
D=True
X,Y=latch(D,E)


s = Solver()
s.add(And(Not(Y),X))
print(s.check())

print(s.model())