from collections import Conter

gazeta = input().split()
zapiska = input().split()
print(Conter(dict(gazeta)) - Conter(dict(zapiska)))

