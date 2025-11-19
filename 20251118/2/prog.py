s = input()
while s != '':
    print(s.encode('latin1', errors='replace').decode('CP1251', errors='replace'))
    s = input()
