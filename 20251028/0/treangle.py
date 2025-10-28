class Rectangle:
    rectcnt = 0
    def __init__(self, x_1, y_1, x_2, y_2):
        self.x_1, self.y_1, self.x_2, self.y_2 = x_1, y_1, x_2, y_2
        self.__class__.rectcnt += 1

    def __str__(self):
        return f"({self.x_1},{self.y_1})({self.x_1},{self.y_2})({self.x_2},{self.y_2})({self.x_2},{self.y_1}), count={self.__class__.rectcnt}"
    
a=Rectangle(1,2,3,4)
a=Rectangle(1,2,3,4)
a=Rectangle(1,2,3,4)
a=Rectangle(1,2,3,4)
a=Rectangle(1,2,3,4)
print(a)

Rectangle.__dict__["rectcnt"]
print(Rectangle.__dict__["rectcnt"])
r=Rectangle(1,2,3,4)
print(Rectangle.__dict__["rectcnt"])

getattr(r, "rectcnt")
# getattr(r, "rectcntttttt") #error
getattr(r, "rectcnt", "Booooo")

setattr(r, "SD", 123)
print(r.SD)

setattr(r, "12345665!@$%$#@!!!#@$#@", 1000)
print(dir(r))