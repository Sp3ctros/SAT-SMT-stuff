from cvc5.pythonic import *


## como é em um contexto de mod 2^8, podemos representar esse sistema de congruencia como variavesi com 8 bits.
x = BitVec('x', 8) 
s = SolverFor('QF_BV')  ##sistema binario sem quantificadores.

s.add(x * 5 == 1) ##assertion

result = s.check() ##checks if the assertions in the given solver plus the assumption are consistent or not.
print("result: ", result) ##prints sat or unsat
print(s.model()) ##printa um model referente ao ultimo check.
