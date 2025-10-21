from itertools import tee, islice

def slide(seq, n):
    s_iter = iter(seq)
    k = 0
    while (True):
        i1, i2 = tee(s_iter)
        s = list(islice(i1, k, k+n))
        if s:
            for i in s:
                yield i
        else:
            break
        s_iter = i2
        k += 1
    pass
        

import sys
exec(sys.stdin.read())