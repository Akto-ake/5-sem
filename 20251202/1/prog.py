import asyncio

async def writer(q, d, ev):
    i = 0
    while True:
        await asyncio.sleep(d)
        if ev.is_set():
            break
        await q.put(f'{i}_{d}')
        i += 1

async def stacker(q, st, ev):
    while True:
        await asyncio.sleep(0)
        if ev.is_set():
            break
        try:
            st.append(q.get_nowait())
        except Exception:
            continue

async def reader(st, k, d, ev):
    await asyncio.sleep(d)
    while k:
        if not st:
            await asyncio.sleep(0.1)
            continue
        print(st.pop())
        k -= 1
        await asyncio.sleep(d)

    ev.set()

async def main():
    d1, d2, d3, k = input().split(',')
    d1, d2, d3, k = int(d1), int(d2), int(d3), int(k)
    q, st, e = asyncio.Queue(), [], asyncio.Event()
    await asyncio.gather(writer(q, d1, e), writer(q, d2, e),stacker(q, st, e), reader(st, k, d3, e))

asyncio.run(main())