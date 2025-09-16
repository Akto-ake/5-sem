a = int(input())
f1 = '+' if a%50 == 0 else '-'
f2 = '+' if a%25 == 0 and a%2 else '-'
f3 = '+' if a%8 == 0 else '-'
print(f'A{f1} B{f2} C{f3}')