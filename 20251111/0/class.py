class A:
    def fun(*args):
        print(f'1: {args}')

    @classmethod
    def cfun(*args):
        print(f'2: {args}') #нулевым элементом добавляется экземпляр класса

    @staticmethod
    def sfun(*args):
        print(f'3: {args}')

print(A.fun)
print(A.cfun)
print(A.sfun)

print(A.fun(1, 2, 3))
print(A.cfun(1, 2, 3))
print(A.sfun(1, 2, 3))