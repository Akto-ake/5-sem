from itertools import product
print(*sorted("".join(name) for name in product("TOR", repeat=int(input())) if "".join(name).count("TOR") == 2), sep=', ')