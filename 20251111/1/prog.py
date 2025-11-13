
def objcount(n):
    class Istype(n):
        counter = 0
        def __init__(self, *args, **kwargs):
            self.__class__.counter += 1
            if getattr(n, "__init__", None):
                super().__init__(*args, **kwargs)

        
        def __del__(self):
            self.__class__.counter -= 1
            if getattr(n, "__del__", None):
                super().__del__()
    return Istype 

import sys
exec(sys.stdin.read())