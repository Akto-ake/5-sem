from itertools import repeat

def repeater(seq, n):
    for el in seq:
        yield from repeat(el, n)

print(list(repeater(iter("QWE"), 5)))