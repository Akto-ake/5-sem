# d = {i*2+1: f"{i}" for i in range (2,7)}

# print(d)

# Посчитать количество вхождений каждого уникального слова в тексте (слова разделены пробелами) с помощью dict

s = 'abc def abc qwert def'
c = {}
s = s.split(' ')
for i in s:
    c[i] = c.setdefault(i, 0) + 1
print(c)