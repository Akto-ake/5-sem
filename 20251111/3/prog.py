class Vowel:
    __slots__ = list("aouiey")
    answer = 42

    def __init__(self, **args):
        for i in args:
            try:
                setattr(self, i, args[i])
            except KeyError:
                setattr(self, i, None)
    
    @property
    def answer(self):
        return 42
    
    @answer.setter
    def answer(self, value):
        raise AttributeError

    def __getattribute__(self, value):
        if value in list("aouiey"):
            if not value in object.__getattribute__(self, "__slots__"):
                raise AttributeError
        return object.__getattribute__(self, value)

    def __setattr__(self, obj, value):
        if obj == 'full':
            pass
        elif not obj in self.__slots__:
            raise AttributeError
        object.__setattr__(self, obj, value)

    def __str__(self):
        c = []
        for i in "aeiouy":
            try:
                s = str(i) + ': ' + str(getattr(self, i))
                c.append(s)
            except AttributeError:
                pass
        
        return ', '.join(c)
    
    @property
    def full(self):
        for i in list("aouiey"):
            try:
                object.__getattribute__(self, i)
            except AttributeError:
                return False
        return True

    @full.setter
    def full(self, value):
        pass

import sys
exec(sys.stdin.read())
