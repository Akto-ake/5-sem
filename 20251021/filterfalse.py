from itertools import filterfalse

def div(n, seq):
    yield from filterfalse(lambda x: x%n, seq)
# print(filterfalse(lambda x: x<5, [1,4,6,3,8]))

print(list(div(5, range(33))))
# пример filterfalse() с делимостью на n, а не на 2