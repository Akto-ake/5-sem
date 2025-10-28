class Rectangle:
    rectcnt = 0
    def __init__(self, x_1, y_1, x_2, y_2):
        self.x_1, self.y_1, self.x_2, self.y_2 = x_1, y_1, x_2, y_2
        self.__class__.rectcnt += 1
        setattr(self, f'rect_{self.rectcnt}', self.rectcnt)

    def __str__(self):
        return f"({self.x_1},{self.y_1})({self.x_1},{self.y_2})({self.x_2},{self.y_2})({self.x_2},{self.y_1}), count={self.__class__.rectcnt}"
        # return f"[{self.rectcnt}], ({})"
    
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def __eq__(self, other):
        return abs(self) == abs(other)

    def __mul__(self, other):
        return self.__class__(self.x_1 * other, self.y_1 * other, self.x_2 * other, self.y_2 * other)

    __rmul__ = __mul__

    def __abs__(self):
        return abs(self.x_1 - self.x_2) * abs(self.y_1 - self.y_2)
    
    # def __getitem__(self, idx):
    #     return ((self.x_1, self.y_1), (self.x_1, self.x_2), (self.x_2, self.y_1), (self.x_2, self.y_2))[idx]

    # def __iter__(self):
    #     coord = self.x_1, self.y_1, self.x_2, self.y_2
    #     pairs = (0.1), (0,3), (2, 3), (2, 1)
    #     return ((coord[x], coord[y]) for x, y in pairs)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __del__(self):
        print("QQ")
        self.__class__.rectcnt -= 1
        print("reduce count: ", self.__class__.rectcnt)
        return
# class D:
#     s = "QWRTREWEWQWWW"
#     def __getitem__(self, idx):
#         return self.s[idx]

a=Rectangle(1,2,3,4)
r=Rectangle(1,1,1,1)
print(a < r)

print(r*2)
print (4*r)

r*=2
print(r)

# d = D()
# print(d[7])

# print(a[1])

print(bool(a))

del(a)

for dot in Rectangle(1,1,6,7):
    print(dot)