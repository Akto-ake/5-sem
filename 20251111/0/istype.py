# ----------------- 1st task ----------------

# def istype(typ):
#     def muldec(f):
#         def decor(*args):
#             for i in args:
#                 if not isinstance(i, typ):
#                     raise TypeError
#             return f(*args)
#         return decor
#     return muldec

# @istype(int)
# def fun(a, b, c):
#     return 2*a+b+c

# print(fun(2,3,4))

# ----------------- 2nd - class task ----------------

class Istype:
    def __init__(self, t):
        self.typ = t
    
    def __call__(self, f):
        def decor(*args):
            for i in args:
                if not isinstance(i, self.typ):
                    raise TypeError
            return f(*args)
        return decor


@Istype(int)
def fun(a, b, c):
    return 2*a+b+c

print(fun(2,3,4))

# def istype(typ):
#     class Istype:
#         def __init__(self, t):
#             self.typ = t
        
#         def __call__(self, f):
#             def decor(*args):
#                 for i in args:
#                     if not isinstance(i, self.typ):
#                         raise TypeError
#                 return f(*args)
#             return decor
#     return Istype 