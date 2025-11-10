# -------------------- 1st task ------------------
#  class E1(Exception):
#     pass

# class E2(Exception):
#     pass

# class E3(E2):
#     pass

# for i in [Exception(), E1(), E2(), E3()]:
#     try:
#         raise i
#     except E3:
#         print('E3')
#     except E2:
#         print('E2')
#     except E1:
#         print('E1')

#     except Exception:
#         print("EEEEEEE")
# #базовый класс съест производный

# for i in [Exception(), E1(), E2(), E3()]:
#     try:
#         raise i
#     except E3:
#         print('E3')
#     except E2:
#         print('E2')
#     except Exception:
#         print("EEEEEEE")
#     except E1:
#         print('E1')


# -------------------- 2nd task ------------------
# while True:
#     try:
#         a = int(input())
#     except ValueError:
#         print('try again')
#     else:
#         print('congrat')
#         exit()

# -------------------- 3rd task ------------------

# def itemget(collection, index):
#     return collection[index]

# def safeindex(function, *args):
#     try:
#         return function(*args)
#     except IndexError:
#         return None
        
# print(list(safeindex(itemget, "qwe", i) for i in range(5)))

# # исключение TypeError (например, safeindex(itemget, "qwe", "qwe")) не перехватывается
# # print(safeindex(itemget, "qwe", "qwe"))

# -------------------- 4th task ------------------

# def  div(a, b, eps):
#     if abs(b) < eps:
#         raise ZeroDivisionError
#     return a / b

# # a, b, eps = 1, 3, 0.0002
# a, b, eps = 1, 0.00000004, 0.0002
# try:
#     print(div(a, b, eps))

# except ZeroDivisionError:
#     print('oh no')

        
# -------------------- 5th task ------------------

class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass

class E(C, B): pass
print(E.__mro__)

# class E(B, C): pass # error
# print(E.__mro__)

class E(C, A): pass
print(E.__mro__)

class E(D, A): pass
print(E.__mro__)

class E(D, B): pass
print(E.__mro__)

# class E(D, C): pass # error
# print(E.__mro__)

# class E(C, D): pass # error
# print(E.__mro__)

for i in [A, B, C, D]:
    for j in [A, B, C, D]:
        try:
            class E(i, j): pass
        except TypeError:
            pass
        else:
            print(i, j)