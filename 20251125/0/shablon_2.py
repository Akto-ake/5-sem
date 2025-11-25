# a = eval(input())
while s := input():
    s = s.split() 
    match s:
        case ["mov", r1, r2]:
            print("movig", r1, "to", r2)
        case ["push" | "pop" as cmd, *reglist]:
            print(f"{cmd}ing", *reglist)
        case [cmd, r1]:
            print("making", cmd, "with", r1)
        case _:
            print("Err")
