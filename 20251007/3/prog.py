fl = 1
a = input()
k = len(a) - 2
count_gas = 0
count_vod = 0
count_str = 0
while(fl):
    a = input()
    if a[1] == '.':
        count_gas += k
        count_str += 1
    elif a[1] == '~':
        count_vod += k
        count_str += 1
    elif a[1] == '#' :
        fl = 0

print(f'count_vod: {count_vod}, stolb: {count_str}')

print('#' * (count_str+2))
line_water = count_vod // count_str if count_vod % count_str == 0 else count_vod // count_str + 1

for i in range(k-line_water):
    print('#' + '.' * count_str + '#')

for i in range(line_water):
    print('#' + '~' * count_str + '#')

print('#' * (count_str+2))

dol_gas = str(count_gas) + '/' + str(count_str * k)
dol_wat = str(count_vod) + '/' + str(count_str * k)

s_point = '.' * count_gas
s_water = '~' * count_vod

l = len(dol_wat) + len(s_water) - len(s_point)

print(f"{s_point} {dol_gas:>{l}}")
print(f"{s_water} {dol_wat}")
