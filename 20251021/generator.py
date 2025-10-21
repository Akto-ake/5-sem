def f(n):
    s = 0
    for i in range(1, n+1):
        s += 1/(i**2)
        yield s

e = f(5)

print(*e)

# e = (i*2+1 for i in range(10) if i%3)
def pri(sed):
    print(*sed)

pri(i*2+1 for i in range(10) if i%3)

print(sum(1/i**2 for i in range(1, int(input()) + 1)))