a = []
for i in range(5, 16):
    a.append(i)

b = []
for i in 'abcdefghijk':
    b.append(i)

a[4:8] = b[-5:]
print(a)