from math import dist

class Triangle:
    def __init__(self, t_1, t_2, t_3):
        self.x1, self.y1 = t_1
        self.x2, self.y2 = t_2
        self.x3, self.y3 = t_3
        # print(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)


    def __abs__(self):
        r12 = dist((self.x1, self.y1), (self.x2, self.y2))
        r23 = dist((self.x3, self.y3), (self.x2, self.y2))
        r13 = dist((self.x1, self.y1), (self.x3, self.y3))

        if (r12 < (r23 + r13)) and (r23 < (r12 + r13)) and (r13 < (r23 + r12)):
            return 0.5 * abs(self.x1*(self.y2-self.y3) + self.x2*(self.y3-self.y1) + self.x3*(self.y1-self.y2))
        else:
            #triangle impossible
            return 0
        
    def __bool__(self):
        return bool(abs(self))
    
    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def __contains__(self, other):
        #один и тот же треугольник
        if not((self < other) or (other < self)):
            return True
        # вложенный треугольник пустой
        if not(abs(other)):
            return True
        # внешний треугольник пуст, а внутренний нет
        if not(abs(self)):
            return False
        s = abs(self)
        s1 = abs(Triangle((self.x1, self.y1), (self.x2, self.y2), (other.x1, other.y1)))
        s2 = abs(Triangle((self.x1, self.y1), (self.x3, self.y3), (other.x1, other.y1)))
        s3 = abs(Triangle((self.x3, self.y3), (self.x2, self.y2), (other.x1, other.y1)))
        if ((s1 + s2 + s3) > s - 0.0001) and ((s1 + s2 + s3) < s + 0.0001):
            s11 = abs(Triangle((self.x1, self.y1), (self.x2, self.y2), (other.x2, other.y2)))
            s22 = abs(Triangle((self.x1, self.y1), (self.x3, self.y3), (other.x2, other.y2)))
            s33 = abs(Triangle((self.x3, self.y3), (self.x2, self.y2), (other.x2, other.y2)))
            if ((s11 + s22 + s33) > s - 0.0001) and ((s11 + s22 + s33) < s + 0.0001):
                s111 = abs(Triangle((self.x1, self.y1), (self.x2, self.y2), (other.x3, other.y3)))
                s222 = abs(Triangle((self.x1, self.y1), (self.x3, self.y3), (other.x3, other.y3)))
                s333 = abs(Triangle((self.x3, self.y3), (self.x2, self.y2), (other.x3, other.y3)))
                if ((s111 + s222 + s333) > s - 0.0001) and ((s111 + s222 + s333) < s + 0.0001):
                    return True
        return False
        
    def __and__(self, other):
        # оба пустые
        if not(abs(self)) and not(abs(other)):
            return False
        #один и тот же треугольник
        if not((self < other) or (other < self)):
            return True
        # какой то треугольник пустой
        if not(abs(self)) or not(abs(other)):
            return False
        # треугольник вложен
        if self in other:
            return False
        if other in self:
            return False

        # for self 1 line
        b1 = (self.y1 - self.y2) / (self.x1 - self.x2) #0
        a1 = self.y1 - b1* self.x1 # 1

        # for other 1 line
        b2 = (other.y1 - other.y2) / (other.x1 - other.x2) #0
        a2 = other.y1 - b2* other.x1 # 1

        if b1 != b2:
            x_solve = (a1 - a2) / (b2 - b1)
            y_solve = a1 + b1 * x_solve
            if (x_solve > min(self.x1, self.x2)) and (x_solve < max(self.x1, self.x2)) and (y_solve > min(self.y1, self.y2)) and (y_solve < max(self.y1, self.y2)):
                return True
        
        # for other 2 line
        b2 = (other.y1 - other.y3) / (other.x1 - other.x3) #0
        a2 = other.y1 - b2* other.x1 # 1

        if b1 != b2:
            x_solve = (a1 - a2) / (b2 - b1)
            y_solve = a1 + b1 * x_solve
            if (x_solve > min(self.x1, self.x2)) and (x_solve < max(self.x1, self.x2)) and (y_solve > min(self.y1, self.y2)) and (y_solve < max(self.y1, self.y2)):
                return True

        # for other 3 line
        b2 = (other.y2 - other.y3) / (other.x2 - other.x3) #0
        a2 = other.y2 - b2* other.x2 # 1

        if b1 != b2:
            x_solve = (a1 - a2) / (b2 - b1)
            y_solve = a1 + b1 * x_solve
            if (x_solve > min(self.x1, self.x2)) and (x_solve < max(self.x1, self.x2)) and (y_solve > min(self.y1, self.y2)) and (y_solve < max(self.y1, self.y2)):
                return True
        # --------------------------------------------------
        # for self 2 line
        b1 = (self.y1 - self.y3) / (self.x1 - self.x3) #0
        a1 = self.y3 - b1* self.x3 # 1

        # for other 1 line
        b2 = (other.y1 - other.y2) / (other.x1 - other.x2) #0
        a2 = other.y1 - b2* other.x1 # 1

        if b1 != b2:
            x_solve = (a1 - a2) / (b2 - b1)
            y_solve = a1 + b1 * x_solve
            if (x_solve > min(self.x1, self.x3)) and (x_solve < max(self.x1, self.x3)) and (y_solve > min(self.y1, self.y3)) and (y_solve < max(self.y1, self.y3)):
                return True
        
        # for other 2 line
        b2 = (other.y1 - other.y3) / (other.x1 - other.x3) #0
        a2 = other.y1 - b2* other.x1 # 1

        if b1 != b2:
            x_solve = (a1 - a2) / (b2 - b1)
            y_solve = a1 + b1 * x_solve
            if (x_solve > min(self.x1, self.x3)) and (x_solve < max(self.x1, self.x3)) and (y_solve > min(self.y1, self.y3)) and (y_solve < max(self.y1, self.y3)):
                return True

        # for other 3 line
        b2 = (other.y2 - other.y3) / (other.x2 - other.x3)
        a2 = other.y2 - b2* other.x2 # 1

        if b1 != b2:
            x_solve = (a1 - a2) / (b2 - b1)
            y_solve = a1 + b1 * x_solve
            if (x_solve > min(self.x1, self.x3)) and (x_solve < max(self.x1, self.x3)) and (y_solve > min(self.y1, self.y3)) and (y_solve < max(self.y1, self.y3)):
                return True
        # --------------------------------------------------
        # for self 3 line
        b1 = (self.y2 - self.y3) / (self.x2 - self.x3) #0
        a1 = self.y3 - b1* self.x3 # 1

        # for other 1 line
        b2 = (other.y1 - other.y2) / (other.x1 - other.x2) #0
        a2 = other.y1 - b2* other.x1 # 1

        if b1 != b2:
            x_solve = (a1 - a2) / (b2 - b1)
            y_solve = a1 + b1 * x_solve
            if (x_solve > min(self.x2, self.x3)) and (x_solve < max(self.x2, self.x3)) and (y_solve > min(self.y2, self.y3)) and (y_solve < max(self.y2, self.y3)):
                return True
        
        # for other 2 line
        b2 = (other.y1 - other.y3) / (other.x1 - other.x3) #0
        a2 = other.y1 - b2* other.x1 # 1

        if b1 != b2:
            x_solve = (a1 - a2) / (b2 - b1)
            y_solve = a1 + b1 * x_solve
            if (x_solve > min(self.x2, self.x3)) and (x_solve < max(self.x2, self.x3)) and (y_solve > min(self.y2, self.y3)) and (y_solve < max(self.y2, self.y3)):
                return True

        # for other 3 line
        b2 = (other.y2 - other.y3) / (other.x2 - other.x3)
        a2 = other.y2 - b2* other.x2 # 1

        if b1 != b2:
            x_solve = (a1 - a2) / (b2 - b1)
            y_solve = a1 + b1 * x_solve
            if (x_solve > min(self.x2, self.x3)) and (x_solve < max(self.x2, self.x3)) and (y_solve > min(self.y2, self.y3)) and (y_solve < max(self.y2, self.y3)):
                return True
        return False
import sys
exec(sys.stdin.read())