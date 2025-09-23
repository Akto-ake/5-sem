a = input().split()
# a = eval(input())
for i in a:
    if int(i) % 2:
        print(i)
        break
else:
    print(0)