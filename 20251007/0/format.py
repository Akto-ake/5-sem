# g = 1.345e2
# print(f"{g*2:9.3}")

# k = -1234
# print(f"{k:09}")
# print(f"{k:@^20}")

# a,b = 100500, 20

# print(f"{a:{b}}")
k = (len(str(bin(35))))
l = (len(str(hex(35))))
print(k)
for i in range(12, 35):
    
    print(f"{bin(i):<{k}} = {hex(i):{l}}")
