a,b,c = eval(input())
if a > 0 and b > 0 and c > 0 and a+b+c > 2 * max(a,b,c):
    print("triangle")
else:
    print("not triangle")
