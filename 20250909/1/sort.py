import sys
exec(sys.stdin.read())

a = eval(input())
a.sort()
print(*a, sep=', ')