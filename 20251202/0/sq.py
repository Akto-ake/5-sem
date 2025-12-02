import asyncio

async def doubler(a):
    return a*2

async def squarer(a):
    return a*a

async def main(a, b):
    
    a, b = await asyncio.gather(squarer(a), squarer(b))
    print(a, b)
    a, b = await asyncio.gather(doubler(a), doubler(b))
    print(a, b)


asyncio.run(main(*(eval(input()))))