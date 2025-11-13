class Num:
    m_n = list()
    def __get__(self, obj, cls):
        if obj in self.m_n:
            return obj._value
        return 0
    
    def __set__(self, obj, val):
        if getattr(val, "real", None):
            obj._value = val
        elif getattr(val, "__len__", None):
            obj._value = len(val)
        self.m_n.append(obj)



import sys
exec(sys.stdin.read())