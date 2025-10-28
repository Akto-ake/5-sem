class C:
    f = 123


c = C()
c.qwe="qwer"
print(callable(C))
print(c.qwe)
print(dir(C))

def fun(*args):
    print("<", *args, ">")
C.ooo=fun
print(C.ooo)

print(c.f)
C.f = 100500
print(c.f)

