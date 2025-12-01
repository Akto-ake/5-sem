class dump(type):
    def __new__(metacls, name, parents, namespace, **kwd):
        def m(f):
            def pr(self, *arg, **kwd):
                print(f'{f.__name__}: {arg}, {kwd}')
                return f(self, *arg, **kwd)
            return pr
                
        for i, val in namespace.items():
            if hasattr(val, "__globals__"):
                namespace[i] = m(val)
        return super().__new__(metacls, name, parents, namespace)

import sys
exec(sys.stdin.read())
