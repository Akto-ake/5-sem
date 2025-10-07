from decimal import Decimal
from decimal import getcontext
from fractions import Fraction



# def multiplier(x, y, Type):
#     return Type(x) * Type(y)


# print(multiplier("1/6", "2/3", Fraction))
# print(multiplier("1.6", "2.3", Decimal))
# print(multiplier("1.6", "2.3", float))

a = Decimal("444.44")
getcontext().prec = 2
print(a.sqrt())

