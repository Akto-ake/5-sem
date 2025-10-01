def Pareto(*a):

    b = a
    
    for i in a:
        for j in a:
            if i == j:
                continue
            
            # print('j: ', j)
            if i[1]<=j[1] and i[0]<=j[0] and (i[1]<j[1] or i[0]<j[0]):
                ind = b.index(i)
                b = b[:ind] + b[ind+1:]
                break
    return  b

a = list(eval(input()))
print(Pareto(*a))