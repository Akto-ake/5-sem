# a,b,c = map(float, input().split())
# print(a,b,c)


# a,b,c = map(int, (("123121111", 4), ("aaaaa", 16), ("123451234234", 10)))

from itertools import starmap, combinations, combinations_with_replacement
a,b,c = starmap(int, (("123121111", 4), ("aaaaa", 16), ("123451234234", 10)))
print(a,b,c)


print(list(combinations("qwercv", 3)))

print(list(starmap(str.__add__, combinations_with_replacement("1234567890", 2))))

from itertools import product
print(list(starmap(str.__add__, product('12345678', 'abcdefgh'))))

print(*("".join(name) for name in product('12345678', 'abcdefgh')))