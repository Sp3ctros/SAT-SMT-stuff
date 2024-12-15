from cvc5.pythonic import *
a, b = Ints('a b')

solve(b + 20 == 2 * a, a + 10 == 2*b)