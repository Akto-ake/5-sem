from math import *

def F(a, b, c):
    s, t, u = eval(f"lambda x: {a}"), eval(f"lambda x: {b}"), eval(f"lambda x, y: {c}")
    def func(x):
        if type(eval(x)) is int:
            a = int(x)
        elif type(eval(x)) is float:
            a = float(x)
        elif type(eval(x)) is complex:
            a = complex(x)
        else:
            a =  list(eval(x))
        return u(s(a), t(a))
    return func


a, b, c = eval(input())
x = input()
k = F(a, b, c)
print(F(a, b, c)(x))