a = input().split()
fl = 0
for i in a:
    if '13' in i:
        print('find 13')
        fl = 1
if not fl:
    print('13 not find')