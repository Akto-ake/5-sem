s = list(input().lower())
flag_first = 0
c = []
# print(s)
for j in s:
    if str.isalpha(j):
        # print(j)
        if not flag_first:
            s1 = j
            flag_first = 1
        else:
            para = s1 + j
            # flag_first = 0
            if not para in c:
                c.append(str(para))
            s1 = j
            
    else:
        flag_first = 0
print(len(c))
