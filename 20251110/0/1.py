# class A:
#     a = 123
#     b = 11
#     v = 1
#     def __init__(self, val):
#         self.val = val
    
#     def __add__(self, other):
#         return self.__class__(self.val + other.val)
    
#     def __str__(self):
#         return f"<{self.val}>"

# class B(A):
#     a = 1
#     v = 2
    
#     def __str__(self):
#         return f"<((((((({self.val})))))))>"

# ------------------ first task --------------
# b = B()
# b.v = 3
# print(b.v)
# del b.v
# print(b.v)

# del B.v
# print(b.v)

# ------------------ second task --------------
# a = A(5)
# print(a)

# print(a + A(2))

# b = B(1)
# print(b)
# print(b + B(11))

#  ------------------ 3rd task --------------
# # C = type('CC', (), {'a': 213, '__str__': lambda self: f'{self.__class__.__name__}'})
# C = type('CC', (), {'a': 213, '__str__': lambda self: f'{self.__class__.__name__}', "13e34egeewro303u032rh": 336})
# c = C()
# print(C)
# print(C.a)
# print(c)
# # print(c.13e34egeewro303u032rh)  #error
# print(C.__dict__["13e34egeewro303u032rh"])

# ------------------ 4th task --------------

# D = type('DDD', (), {'Q-Q!': 11})
# F = type('FFF', (D, ), {'Q-Q!': 'hehe'})

# d = D()
# f = F()
# print(D.__dict__["Q-Q!"])
# print(F.__dict__["Q-Q!"])


# A = type('A', (), {\
#     '__init__': lambda self, val: setattr(self.__class__, 'Q-Q!', val), \
#     '__str__': lambda self: f'<{self.__class__._dict__["Q-Q!"]}>'})

# ------------------ 5th task --------------
# class A:
#     __f = 123

# class B(A):
#     __f = 1

# print(dir(A))
# print(dir(B))

# print(B._A__f)
# print(B._B__f)

# ------------------ 6th task --------------
# A = type('A', (), {'__a': 'hi'})

# B = type('B', (A, ), {'__a': 'hello'})

# print(dir(A))
# print(dir(B))

# print(B.__a)
# del B.__a
# print(B.__a)

# ------------------ 7th task --------------
# class A:
#     def __init__(self, val):
#         self.val = val

# class B(A):
#     def __init__(self, val):
#         print("Do it A")
#         super().__init__(val)
#         print(f'<{self.val}>')

# b = B(1234)

# ------------------ 8th task --------------
# class A:
#     def __init__(self, val):
#         self.val = val

# class B(A):
#     def __init__(self, val):
#         print("Do it A")
#         super().__init__(val)
#         print(f'<{self.val}>')


# class C(B):
#     def __init__(self, val):
#         print("Do it A")
#         super().__init__(val)
#         print(f'<{self.val}>')


# ------------------ 9th task --------------
class A:  
    def __str__(self):
        return 'A'

class B(A):
    def __str__(self):
        return super().__str__() + ':B'

class C(B):
    def __str__(self):
        return super().__str__() + ':C'
print(C())