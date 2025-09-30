def average(a, *alot):
    return (sum(alot) + a) / (len(alot) + 1)


print(average(1,2,3,4,5,6))