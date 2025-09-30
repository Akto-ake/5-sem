# 1) написать примитивно-рекурсивную функцию которая вызывает себя N раз в глубину (уменьшая параметр на 1 до 0)

# def func(n):
#     return func(n-1) if n > 0 else 1
#     # print(n)

# n = 100
# print(func(n))


# 2) Написать рекурсивную функцию binN(n, ones, base=0), которая выводит в порядке убывания все натуральные числа, для двоичной записи которых достаточно n-ones нулей и ones единиц. Лидирующие нули считаются.

# Пример работы binN(*eval(input())):

# def binN(n, ones, base=0):
#     if (n and ones):
#         binN(n-1, ones-1, base*2+1)
#         binN(n-1, ones, base*2)
#     elif n:
#         binN(n-1, ones, base*2)
#     elif ones:
#         return 0
#     else:
#         print(base)
#         return 0

# print(binN(*eval(input()))) #4,2


# 3) функционал

# def f(x):
#     return x*2

# def g(x):
#     return x*3 +1
# def F(f1, f2):
#     def func(x):
#         return f1(x) + f2(x)
#     return func

# print(f(2))
# print(g(2))


# s = F(f, g)
# print(s(2))


# # 4) Напишите функционал, MINF(f₀, f₁, …) которому передаётся произвольное количество функций от одной переменной fi(x), а он возвращает функцию от одной переменой g(x) — наименьшее значение среди fi(x).

# def f(x):
#     return x/2

# def g(x):
#     return x/3

# def q(x):
#     return x/4

# def MinF(*fun):
#     def func(x):
#         return min([f(x) for f in fun])
#     return func

# s = MinF(f, g, q)
# print(s(6))


# MINF = lambda *func: lambda x: min([f(x) for f in func])
# print(s.__closure__[0].cell_contents)

# 5)  Напишите функцию с параметрами a и b, которая с использованием замыкания создает функцию-вычислитель линейного двучлена a*x+b



def Mn(a, b):
    def func(x):
        return a*x+b
    return func


