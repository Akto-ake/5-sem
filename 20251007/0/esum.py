from decimal import Decimal
from decimal import getcontext
from fractions import Fraction

def esum(N, one):
    E = 0
    F = one
    for i in range(1, N+1):
        F *= (i + 1)
        E += (one / F)
    print(E)
