lst = [i*2 +1 for i in range(10)]
lst = [i*2 +1 for i in range(10) if i!=6]
print(lst)

# a = [[0]*4] *3 # получим одинакове объекты
# a = [[0]*4 for i in range(3)] #тут они будут не связаны

# a = 122344566
a, b = eval(input())
print([i for i in range(a,b) if i % 2 == 1 and '3' not in str(i)])

print(any([], [], 0, 0, 6))