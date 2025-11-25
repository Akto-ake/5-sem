# Метаклассы

# C = type("C", (), {"var":100500, "__init__": lambda self, x: setattr(self, "var", x)} )
# print(C.var)
# c = C(123)
# print(c.var)

class ctype(type):
    @classmethod
    def __prepare__(metacls, name, parents, **kwd):
        print("PREPARE", name, parents, kwd)
        return super().__prepare__(name, parents, **kwd)
    
    def __new__(metacls, name, parents, ns, **kwd):
        print(("NEW", metacls, name, parents, ns, kwd))
        return super().__new__(metacls, name, parents, ns)

    def __init__(cls, name, parents, namespace, **kwd):
        print("INIT", cls, parents, namespace, kwd)
        return super().__init__(name, parents, namespace)
    
    def __call__(cls, *args, **kwd):
        print("CALL", cls, args, kwd)
        return super().__call__(*args, **kwd)


class C(int, metaclass=ctype, param="TARAM"):
    A = 100500

c = C()
    
