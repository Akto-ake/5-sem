import sys

s_in = sys.stdin.buffer.read()

n = s_in[0]
tail = s_in[1:]
c = []
L = len(tail)
for i in range(n):
    # i*L/N …(i+1)*L/N, где i — номер части (от 0 до N-1)
    c.append(tail[i*L//n:(i+1)*L//n])

c = sorted(c)
sys.stdout.buffer.write(bytes([n]) + b"".join(c))
# print(n, L)
