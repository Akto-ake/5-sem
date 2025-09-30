def gen_adders(n):
    adders=[]
    for i in range(n):
        def func(x, y=i):
            return x + y
            #чтобы i в конце не заменилось на одинаковое
        adders.append(func)
    # i = 100400
    return adders #вот тут связывание

s = gen_adders(4)
print(s[3](100))

# print(s[0].__closure__[0].cell_contents)