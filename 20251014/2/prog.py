from math import *

s = input()
d = {}
k_param = 0
count_opr, count_str = 1,0
while True:
    count_str += 1
    if s[0] == ':':
        # :функция переменная_1 переменная_2 … Питоновское_выражение_без_пробелов_от_этих_переменных
        s = s[1:]
        s = s.split(' ')
        py_func = s[-1]
        func = s[0]
        args = s[1:len(s)-1]
        # k_param = len(args)
        d[func] = {py_func: args}
        count_opr +=1
    elif 'quit' in s:
        print(s[6:len(s)-1].format(count_opr, count_str))
        break
    
    else:
        # функция константа_1 константа_2 …
        s = s.split(' ', 1)
        func = s[0]

        formula, val = next(iter(d[func].items()))
        k_param = len(val)
        args = []
        if k_param > 1:
            s = s[1].split(' ')
            args = [int(i) if i.isdigit() else i for i in s]

        elif k_param == 1:
            args = [int(s[1]) if s[1].isdigit() else s[1]]

        # print(d[func], k_param, args)
        check = eval(formula, globals(), dict(zip(val, args)))
        if not check is None:
            print(check)

    s = input()
