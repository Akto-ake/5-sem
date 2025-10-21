def fib(m, n):
    first, second = 1, 0
    for _ in range(m):
        first, second = first + second, first
        # second = 
    for _ in range(n):
        yield first
        first, second = first + second, first
        

import sys
exec(sys.stdin.read())