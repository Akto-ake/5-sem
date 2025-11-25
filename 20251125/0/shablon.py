# a = eval(input())

class CONST:
    A = 100500

match eval(input()):
    case "QWE":
        print("QWE!")
    case "A" | "B" as s: #связыывание
        print("Letter", s)
    # case A: # не српботает, будет просто связанной переменной
    case CONST.A:
        print("stop A")
    case int(n) if n > 0:
        # нулевой элемент в eval можно преобразоать в инт
        print("Positive:", n)
    case int(n):
        print("Int:", n)
    case (0, *tail):
        print("Zero tuple", tail)
    case (float(n) | int(n), *tail):
        print(f"{n} - tuple", tail)
    case _:
        print("UNK")
