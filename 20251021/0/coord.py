def walk2d():
    # var = yield [0,0]
    x, y = 0,0
    while True:
        dx, dy = yield x, y
        # a, b = yield f"<{a}> <{b}>"
        # var[0] += a
        # var[1] += b
        x += dx
        y += dy
p = walk2d()
next(p)

p.send((2, 0))

def seqlen(seq):
    yield from seq
    return(len(seq)) #в StopItaration результат

def glue(*seq):
    for s in seq:
        lenth = yield from seqlen(s)
        yield lenth
list(glue("QWE", range(3)))
# list(glue("QWE", range(3)), (i*2+3 for i in range(3))) # для length не сработает


