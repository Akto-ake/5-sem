fl = 1
k = 0
a = []
b = []
while s:=input():
    L = len(s) // 2 + 1
    if fl:
        a.append(list(eval(s)))
        k += 1
        if (k == L):
            fl = 0
    else:
        b.append(list(eval(s)))

c = []
for i in range(L):
    c_str = []
    for j in range(L):
        v = 0
        for k in range(L):
            v += a[i][k] * b[k][j]
        c_str.append(v)
    c.append(c_str)
for i in c:
    print(*i, sep = ',')