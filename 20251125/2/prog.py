
import math
c = []
# список переменных и их значений
perem = {}

# список меток
goto = {}

while True:
    try:
        s = input()
    except EOFError:
        break

    s = s.strip()

    metk = ''
    if ':' in s:
        start, end = s.split(':', 1)
        metk = start.strip()
        s = end.strip()
    if metk != '':
        goto[metk] = len(c)
    # print(s)
    if ' ' in s:
        s = s.split()

    if not len(s):
        continue
    elif s[0] == 'store' and len(s) == 3:
        try:
            a = float(s[1])
            perem[s[2]] = float(s[1])
            c.append(['store', [s[2], float(s[1])]])
        except Exception:
            perem[s[2]] = 0
            c.append(['store', [s[2], 0]])
    elif (s[0] == 'add' or s[0] == 'mul' or s[0] == 'div' or s[0] == 'sub') and len(s) == 4:
        # if s[0] == 'div' and (s[2] == '0' or perem.get(s[2], 1) == 0):
        #     print(math.inf)
        #     exit()
        c.append([s[0], [s[1], s[2], s[3]]])

    elif (s[0] in ['ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle']) and len(s) == 4:
        c.append([s[0], [s[1], s[2], s[3]]])

    elif s[0] == 'out' and len(s) == 2:
        c.append([s[0], [s[1]]])
    elif s[0] == 'stop' and len(s) == 1:
        c.append([s[0], []])
    # print(c)


for i, j in c:
    if i in ['ifeq','ifne','ifgt','ifge','iflt','ifle']:
        if not j[2] in goto:
            # print('here', j[2])
            exit()
i = 0
while (i >= 0) and (i < len(c)):
    com, l = c[i]

    if com == 'stop':
        break
    elif com == 'store':
        a, b = l
        perem[a] = b
        i += 1
        continue
    elif com == 'add' or com == 'mul' or com == 'div' or com == 'sub':
        a, b, v = l
        try:
            a = float(a)
        except Exception:
            a = float(perem.get(a, 0.0))
        try:
            b = float(b)
        except Exception:
            b = float(perem.get(b, 0.0))
        if ((b == 0) or (b == 0.0)) and com == 'div':
            perem[v] = math.inf
        elif com == 'div':
            perem[v] = a / b
        elif com == 'mul':
            perem[v] = a * b
        elif com == 'add':
            perem[v] = a + b
        elif com == 'sub':
            perem[v] = a - b
        i += 1
        continue
    elif (com in ['ifeq', 'ifne', 'ifgt', 'ifge', 'iflt', 'ifle']):
        a, b, v = l
        try:
            a = float(a)
        except Exception:
            a = float(perem.get(a, 0.0))
        try:
            b = float(b)
        except Exception:
            b = float(perem.get(b, 0.0))

        if (com == 'ifeq' and (a == b)) or \
            (com == 'ifne' and (a != b)) or \
            (com == 'ifgt' and (a > b)) or \
            (com == 'ifge' and (a >= b)) or \
            (com == 'iflt' and (a < b)) or \
            (com == 'ifle' and (a <= b)):
            i = goto[v]
            continue
        i+= 1
        continue
    elif com == 'out':
        print(perem.get(l[0], 0.0))
        i += 1
        continue
    i+=1