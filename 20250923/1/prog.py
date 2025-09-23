a, b = eval(input())
print([i for i in range(a, b) if sum(1 for j in range(1, i//2 + 1) if i % j == 0) == 1])