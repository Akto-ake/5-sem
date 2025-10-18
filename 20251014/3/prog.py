import string

k = int(input())
# print('k: ', k)
s = (input().lower())

z = '0123456789' + string.punctuation
d = {}
while s != '':
    for i in z:
        s = s.replace(i, ' ')
    s = ' '.join(s.split()).split()
    for j in s:
        # print('j: ', j,' len j:', len(j), 'in', 's: ', s)
        if len(j) == k:
            # print('j: ', j, 'in', 's: ', s)

            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    s = (input().lower())
d = sorted(d.items(), key=lambda item: item[1], reverse=True)
max_val = 0
c=[]
for i, j in d:
    if not max_val:
        max_val = j
        c.append(i)
    elif max_val == j:
        c.append(i)
    else:
        break
c = sorted(c)
print(*c)