import collections
import timeit

def f1(s):
    c = {}
    s = s.split(' ')
    for i in s:
        c[i] = c.setdefault(i, 0) + 1
    return c

def f2(s):
    c = {}
    s = s.split(' ')
    cnt = collections.Counter()
    for j in s:
        cnt[j] += 1

    return cnt

# d = {i*2+1: f"{i}" for i in range (2,7)}

# print(d)

# Посчитать количество вхождений каждого уникального слова в тексте (слова разделены пробелами) с помощью dict

s = 'abc def abc qwert def'

# print(f1(s))
# t = timeit.Timer(lambda: f1(s))
# num, total_time = t.autorange()

# print(f"f1.  Количество повторов: {num}")
# print(f"f1.  Общее время: {total_time} секунд")

# print(f2(s))

# t = timeit.Timer(lambda: f2(s))
# num, total_time = t.autorange()

# print(f"f2.  Количество повторов: {num}")
# print(f"f2.  Общее время: {total_time} секунд")


print(' '.join(dict.fromkeys(s.split())))

print(" ".join({w:1 for w in s.split(' ')}))