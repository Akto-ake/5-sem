from math import sin

# W, H = eval(input()) #окно

# A, B = eval(input()) #границы
# for line in range(0, H):
#     x = A + line / H * (B - A) 
#     y = sin(x)
#     k = round((y + 1) * (W-1) /2)
#     print(' '*k, "*")

def scale(a,b,A,B,x):
    return (x-a) * (B - A) / (b-a) +A

W, H = eval(input()) #окно

A, B = eval(input()) #границы
for line in range(0, H):
    x = scale(0, H-1, A, B, line)
    y = sin(x)
    k = round(scale(-1, 1, 0, W-1, y))
    print(' '*k, "*")