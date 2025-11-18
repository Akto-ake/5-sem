s = input()
while s != '':
    print(s.encode('latin1').decode('CP1251'))
    s = input()
