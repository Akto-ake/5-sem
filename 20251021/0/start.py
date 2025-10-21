def genf(n):
    for i in range(n):
        yield i*3+1

e = genf(5)
print(e)
print(*e)