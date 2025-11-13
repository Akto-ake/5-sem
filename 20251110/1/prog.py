class DivStr(__import__('collections').UserString):
    def __init__(self, s =''):
        super().__init__(s)

    def __floordiv__(self, other):
        m_s = []
        k = len(self.data)
        length = k // other
        for i in range(other):
            m_s.append(DivStr(self.data[i*length:(i+1)*length]))
        return iter(m_s)
    
    def __mod__(self, other):
        k = len(self.data)
        length = k % other
        return DivStr(self.data[-1*length:])

import sys
exec(sys.stdin.read())