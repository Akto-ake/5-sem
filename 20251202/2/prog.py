
import asyncio

async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()

    m_fix = middle
    all = start
    
    while start < middle and m_fix < finish:
        if A1[start] <= A1[m_fix]:
            A2[all] = A1[start]
            start += 1
            all += 1
        else:
            A2[all] = A1[m_fix]
            m_fix += 1
            all += 1

    while start < middle:
        A2[all] = A1[start]
        start += 1
        all += 1

    while m_fix < finish:
        A2[all] = A1[m_fix]
        m_fix += 1
        all += 1

    event_out.set()

async def the_end(A1, A2, start, finish, event_in, event_out):
    await event_in.wait()
    for k in range(start, finish):
        A2[k] = A1[k]
    event_out.set()


async def mtasks(A):
    A_cop = A.copy()
    B = [0] * len(A)
    m_res = []

    m_cur = []
    for i in range(len(A)):
        m_cur.append(asyncio.Event())
        m_cur[i].set()

    deep = 1
    AB = 'B'

    while deep < len(A):
        m = []
        for i in range(len(A)):
            m.append(asyncio.Event())
        if AB == 'A':
            A2 = A_cop
            A1 = B
        else:
            A2 = B
            A1 = A_cop

        i = 0
        while i < len(A):
            middle = min(i + deep, len(A))
            finish = min(i + 2 * deep, len(A))

            if middle < finish:
                m_res.append(asyncio.create_task(merge(A1, A2, i, middle, finish, m_cur[i], m_cur[middle], m[i])))
            else:
                m_res.append(asyncio.create_task(the_end(A1, A2, i, finish, m_cur[i], m[i])))

            i += 2 * deep

        m_cur = m
        deep *= 2
        AB = 'A' if AB == 'B' else 'B'

    return m_res, A_cop if AB == 'B' else B


import sys
exec(sys.stdin.read())