def func(a, b):
    if (type(a) != type(b)):
        print("error")
        return -1
    
    if (type(a) in [int, float, complex]):
        return a - b
    
    if (type(a) == tuple):
        c = b #copy for вычитаемого
    
        for i in b:
            if not i in c:
                continue
            if i in a:
                ind = c.index(i)
                c = c[:ind] + c[ind+1:]
                ind_a = a.index(i)
                a = a[:ind_a] + a[ind_a+1:]
        return a
    
    # остались списки только

    c = b
    for i in b:
        if not i in c:
            continue
        if i in a:
            a.remove(i)
            c.remove(i)
    return  a

a, b = eval(input())
print(func(a, b))