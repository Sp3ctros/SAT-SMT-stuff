from cvc5.pythonic import *

U = DeclareSort("U") #cria um sort
b = Const("b", BoolSort()) #cria uma constante booleana B
x, y, z, w = Consts("x y z w", U) #cria constanets pertencentes a U

s = SolverFor('QF_UF') #cria uma logica do tipo QF_UF
s.add(x == (If(b, y, z))) #assertion
s.add(Or((w == y), (w == z)))#assertion
s.add(x != w)#assertion

if s.check() == sat:  
    m = s.model()
    print("\n".join([str(k) + " : " + str(m[k]) for k in m]))