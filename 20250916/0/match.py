match int(input()):
    case 1:
        print("один")
    case 2:
        print("два")
    case 3:
        print("три")
    case a if a % 2 == 0:
        print("четное")
    case _:
        print(f"{a} -- это много")