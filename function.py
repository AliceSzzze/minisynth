from z3 import *

x = Int('x')
f = Function('f', IntSort(), IntSort())
solve (ForAll([x], f(x) == x*x*(x+2)))
