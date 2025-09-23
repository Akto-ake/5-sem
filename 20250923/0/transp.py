a = []
# n = 5
# for i in range(n):
#     # b = eval(input())
#     b = input().split()
#     a.append(b)
# print(a)

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         a[i][j], a[j][i] = a[j][i], a[i][j]
# for j in a:
#     print(j)

while s:=input():
    a.append(list(eval(s)))

if not all([len(line) == len(a) for line in a]):
    print("Not square")
    exit()

for i in range(len(a)):
    for j in range(i+1, len(a)):
        a[i][j], a[j][i] = a[j][i], a[i][j]

for j in a:
    print(*j)
        