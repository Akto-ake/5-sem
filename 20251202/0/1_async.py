#вспомним генераторы

async def meet(n):
    for i in range(n):
        print(f'{i} hi')
    return f'you {n} Bye!'

async def meeting(m):
    for i in range(m):
        res = await meet(3)
        print(f'<{i}> here {res}')
    return 'FIN'

i = meeting(2)
print(i)

try:
    k = 0
    while True:
        print('>>>>>', k)
        i.send(None)
except StopIteration as E:
    print(E.value)