# {i} Упростить final из лекции: написать метакласс sole, запрещающий классу иметь более одного непосредственного родителя

# class final(type):
#     def __new__(metacls, name, parents, namespace):
#         for cls in parents:
#             if isinstance(cls, final):
#                 raise TypeError(f"{cls.__name__} is final")
#         return super().__new__(metacls, name, parents, namespace)

class sole(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError('more than ine')
        return super().__new__(metacls, name, parents, namespace)

class C(metaclass=sole):
    pass
class D(C): pass
class E(C, int): pass

