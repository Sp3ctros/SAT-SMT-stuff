from cvc5.pythonic import *

U = DeclareSort('A')

x, y, z, w = Ints('x y z w')
b = Bool('b')  #

s = SolverFor('QF_UF')

# Adicionando as restrições  
s.add(Or(And(x == y, b), And(x == z, Not(b))))
s.add(Or(w == y, w == z))  # s
s.add(Distinct(x, w))  # Negação de x == w

print(s.check())
