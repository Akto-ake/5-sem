class Dsc:
    def __get__(self, obj, cls):
        print(obj.__class__.x, cls.x)
        return obj._value

    def __set__(self, obj, val):
        obj._value = val

    def __delete__(self, obj):
        obj._value = None

class A:
    data = Dsc()
    x = 100500
    def __init__(self, name):
        self.data = name

    def __str__(self):
        return f'<{self.data}>'