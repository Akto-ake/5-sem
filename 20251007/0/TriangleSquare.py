from decimal import Decimal
from decimal import getcontext

a = input()
fl = 0
if ("." in a):
    fl = 1

a = a.replace(' ', '')
x1, y1, x2, y2, x3, y3 = (eval(a))
max_num = max(len(str(x1)), len(str(x2)), len(str(x3)), len(str(y1)), len(str(y2)), len(str(y3)))
x1 = Decimal(x1)
y1 = Decimal(y1)

x2 = Decimal(x2)
y2 = Decimal(y2)

x3 = Decimal(x3)
y3 = Decimal(y3)

getcontext().prec = max_num + 10

#1-2
r1 = ((x1 - x2) * (x1 - x2) + (y1-y2)*(y1-y2))
r1 = r1.sqrt()
#2-3
r2 = ((x3 - x2) *(x3 - x2) + (y3-y2)*(y3-y2))
r2 = r2.sqrt()
#1-3
r3 = ((x1 - x3) *(x1 - x3)+ (y1-y3)*(y1-y3))
r3 = r3.sqrt()

p = (r1 + r2+ r3) / 2
res = (p * (p-r1) * (p-r2) *(p-r3))
res = res.sqrt()

res = Decimal(res)
# print(max_num)
if fl:
    getcontext().prec = max_num - 1
else:
    getcontext().prec = max_num
res = +res
print(res)