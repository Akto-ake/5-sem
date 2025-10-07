from math import cos
from math import sin
from math import tan
import math

def scale(a,b,A,B,x):
    return (x-a) * (B - A) / (b-a) + A

W, H, A, B, f_str = input().split() #окно и границы
W = int(W)
H = int(H)
A = int(A)
B = int(B)

def f(x):
    return eval(f_str)

screen = [[' '] * W for i in range(H)]

point = 100000
m_x = []
m_y = []

for i in range(point):
    x = A + (B - A) * i / (point - 1)
    m_x.append(x)
    m_y.append(f(x))

min_x, max_x, min_y, max_y = min(m_x),  max(m_x), min(m_y),  max(m_y)

last_y = None
for i in range(0, W):
    x = scale(0, W-1, A, B, i)
    y = f(x)
    k = round(scale(min_y, max_y, 0, H-1, y))
    cur_y = H - k - 1
    
    if (cur_y == 0) :
        screen[cur_y][i] = "*"
        
    if (cur_y == H-1):
        screen[cur_y][i] = "*"
        
    if last_y is not None:
        start = min(last_y, cur_y)
        end = max(last_y, cur_y)

        for j in range(start, end):
            screen[j][i] = "*"
    
    last_y = cur_y

print('\n'.join("".join(line) for line in screen))