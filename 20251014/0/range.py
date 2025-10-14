import timeit


def count(s):
    a = {'a', 'e', 'i', 'o' ,'u'}
    b = set('qwrtypsdfghjklzxcvbnm')
    # print(b)
    sogl, gl = 0,0
    for i in range(len(s)):
        # print(s[i])
        if (s[i] in a):
            gl += 1
        if (s[i] in b):
            sogl += 1  

    return (gl, sogl)
# a, b = {123,13,14,'1234567',14,1,314141414,12222}, {12345,654,12345,432,123543,1,1,1,'asdf',123}
# union - передавать много множеств
# print(a|b)

# s = input()
# a, b = count(s)
# print(f"glasn: {a}, sogl: {b}")

# создаём объект Timer
t = timeit.Timer(lambda: count('asdfghjkjhgfdsasdfgxxccqAFGFSDKKDDKDKDK'))
num, total_time = t.autorange()

print(f"Количество повторов: {num}")
print(f"Общее время: {total_time} секунд")
# print(len(s&gl), len(s&sogl))