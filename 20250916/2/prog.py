a = int(input())
s = 0
while  a > 0 and s + a <= 21:
    s += a
    a = int(input())
else:
    if a < 0:
        print(a)
    else: 
        print(s+a)