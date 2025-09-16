def sum_ch(a):
    s = 0
    while a >= 10:
        s += a%10
        a //= 10
    s += a
    return s

a = int(input())
b = a
for i in range(3):
    s1 = f'{b} * {a} = {a * b if sum_ch(a*b) != 6 else ':=)'}'
    s2 = f'{b} * {a + 1} = {(a+1) * b if sum_ch((a+1)*b) != 6 else ':=)'}'
    s3 = f'{b} * {(a+2)} = {(a+2) * b if sum_ch((a+2)*b) != 6 else ':=)'}'
    print(s1, s2, s3, sep=' ')
    b += 1