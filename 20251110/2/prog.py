
class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(a)
        x1, y1, x2, y2, x3, y3 = int(x1), int(y1), int(x2), int(y2), int(x3), int(y3)
        # print(x1, y1, x2, y2, x3, y3)
    except ValueError:
        raise InvalidInput
    except NameError:
        raise InvalidInput
    except SyntaxError:
        raise InvalidInput
    except TypeError:
        raise InvalidInput
    else:
        s = 0.5 * abs(x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2))
        if s <= 0:
            raise BadTriangle
        return s

a = input()
while a != '':
    try:
        s = triangleSquare(a)
    except InvalidInput:
        print('Invalid input')
    except BadTriangle:
        print('Not a triangle')
    else:
        print(f'{s:.2f}')
    a = input()
