a = list(eval(input()))

for j in range(len(a) - 1):
    for i in range(len(a) - 1 - j):
        if ((a[i] ** 2) % 100) > (a[i+1] ** 2 % 100):
            a[i], a[i+1] = a[i+1], a[i]

print(a)