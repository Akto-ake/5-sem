def pargen():
    var = yield "START"
    while var:
        var = yield f"<{var}>"
    yield "END"


g = pargen()
print(next(g))

print(g.send(123))

print(g.send((1,2)))
print(g.send(()))