from cvc5.pythonic import *
U = DeclareSort("U") # cria um novo sort
f = Function("f", U, U) #funcao de u para U
x = Const("x", U) #constante é uma funcao sem entrada que retorna um valor do sort.
s = SolverFor('QF_UF') #quantifier free uninterpreted functions
s.add(And((f(f(f(x))) == x), (f(f(f(f(f(x))))) == x)))
s.add(Distinct(f(x), x)) # negation of f(x) = x
print(s.check())

#Isso da unsat, pois nao é possivel (f(f(f(x))) == x) e (f(f(f(f(f(x))))) == x sem f(x) = x.
