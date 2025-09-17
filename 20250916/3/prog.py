def sum_ch(a):
    s = 0
    while a >= 10:
        s += a%10
        a //= 10
    s += a
    return s

a = int(input())
i = 0
while i < 3:
    j = 0
    while j < 3:
        if (sum_ch((a+i) * (a + j)) == 6):
            s = ':=)'
        else:
            s = (a + i) * (a +j)
        print(a + i, ' * ', a + j, ' = ', s, sep = '', end = ' ')
        j += 1
    print()
    i +=1