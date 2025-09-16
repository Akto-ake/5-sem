# i = 1
# s = 0
# while c := int(input()):
#     if c == i:
#         s += 1
#     i += 1
# print(s)
# c = int(input())
while c := input():
    if int(c) % 2 == 0:
        print(c)
    if int(c) == 13:
        print("find 13")
        break
else:
    print("Congratulations")