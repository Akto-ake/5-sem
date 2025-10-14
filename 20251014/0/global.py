globals()["A"] = "qwerty"
print(A)

expr= input()
a, b = eval(input())

# d = dict(zip('ab', (a, b)))
print(eval(expr, {"x": a, "y": b}))