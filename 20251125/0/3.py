# На основании Singleton из лекции написать метакласс
# Doubleton. Экземпляров класса, созданных с его помощью, 
# должно быть не больше двух, каждое следующее создание 
# экземпляра должно возвращать по очереди либо один, 
# либо второй.

# class Singleton(type):
#     _instance = None
#     def __call__(cls, *args, **kw):
#         if cls._instance is None:
#              cls._instance = super().__call__(*args, **kw)
#         return cls._instance

class Doubeleton(type):
    _instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = [super().__call__(*args, **kw)]
        return cls._instance

class C(metaclass=Doubeleton): pass
print(*(C() for i in range(7)), sep="\n")