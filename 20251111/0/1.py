# # def fun(a, b):
# #     return 2*a+b

# def dfun(f):
#     def decor(*args):
#         print('>', *args)
#         res = f(*args)
#         print('<', res)
#         return res
#     return decor

# # print(fun(2,3))
# # dfun(fun, 2, 3)

# # dfun(fun)
# # a = dfun(fun)
# # print(a(2,3))

# # fun = dfun(fun)
# # print(fun(2,3))

# @dfun
# def fun(a, b, c):
#     return 2*a+b+c

# print(fun(2, 3, 3))

# ----------------- 1st task ----------------

# def isint(f):
#     def decor(*args):
#         for i in args:
#             if not isinstance(i, int):
#                 raise TypeError
#         return f(*args)
#     return decor

# @isint
# def fun(a, b, c):
#     return 2*a+b+c

# print(fun(2,3,4))

# ----------------- 2nd task ----------------

# def multicall(n):
#     def muldec(fun):
#         def decor(*args):
#             return [fun(*args) for i in range(n)]
#         return decor
#     return muldec

# @multicall(5)
# def fun(a, b):
#     return a*2 + b

# print(fun(2, 3))

# ----------------- 3rd task ----------------

def istype(typ):
    def muldec(f):
        def decor(*args):
            for i in args:
                if not isinstance(i, typ):
                    raise TypeError
            return f(*args)
        return decor
    return muldec

@istype(int)
def fun(a, b, c):
    return 2*a+b+c

print(fun(2,3,4))
