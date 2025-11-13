
class Undead(Exception):
    pass

class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass


def necro(a):
       
    k = a % 3
    if k == 1:
        raise Zombie
    elif k == 2:
        raise Ghoul
    elif k == 0:
        raise Skeleton

    

x, y = eval(input())
for i in range(x, y):
    try:
        necro(i)
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
    except Undead:
        print("Generic Undead")
