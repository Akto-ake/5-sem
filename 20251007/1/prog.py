from decimal import Decimal
from decimal import getcontext
from fractions import Fraction

def dec_frac(string):
    if not('/' in string):
        s = Decimal(int(string))
    else:
        a_0, a_1 = string.split('/')
        s = Decimal(Decimal(int(a_0))/Decimal(int(a_1)))
    return s

a = input().replace(' ', '').split(',')
# print(a)

s = dec_frac(a[0])
w = dec_frac(a[1])

st_a = int(a[2])
k_a = []
for i in range(st_a + 1):
    k_a.append(dec_frac(a[3+i]))

st_b = int(a[3+i+1])
k_b = []
for j in range(st_b + 1):
    k_b.append(dec_frac(a[3+ i +2+j]))

# print(s, w)
# print(st_a, ': ', *k_a)
# print(st_b, ': ', *k_b)

res_a = 0

for i in k_a:
    res_a = res_a * s + i
# print('res_a: ', res_a)

res_b = 0

for i in k_b:
    res_b = res_b*  s + i
# print('res_b: ', res_b)
if res_b == 0:
    print(False)
else:
    print(Decimal(res_a / res_b) == w)
