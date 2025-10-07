F, I, O, Y, C = input().split(' ')
print(F, I, C)

#если город из двух слов:
F, I, O, Y, *C = input().split(' ')
print(F, I, ' '.join(C))