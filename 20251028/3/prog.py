class Maze:
    def __init__(self, N):
        self.N = N
        self.kor = [[set() for i in range(N)] for j in range(N)]

    def __getitem__(self, key):
        x0, y0 = key[0], key[1].start
        x1, y1 = key[1].stop, key[2]
        visited = set()

        sp_point = [(x0, y0)]
        while sp_point:
            x_new, y_new = sp_point.pop()
            if (x_new, y_new) == (x1, y1):
                return True
            
            if not((x_new, y_new) in visited):
                visited.add((x_new, y_new))
                for i, j in self.kor[y_new][x_new]:
                    if (i, j) not in visited:
                        sp_point.append((i, j))
        return False
        
    def __setitem__(self, key, value):
        x0, y0 = key[0], key[1].start 
        x1, y1 = key[1].stop, key[2]
        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1)):
                if value == "·":
                    self.kor[y][x0].add((x0, y + 1))
                    self.kor[y + 1][x0].add((x0, y))
                elif value == "█":
                    self.kor[y][x0].remove((x0, y+1))
                    self.kor[y + 1][x0].remove((x0, y))
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1)):
                if value == "·":
                    self.kor[y0][x].add((x + 1, y0))
                    self.kor[y0][x+1].add((x, y0))
                elif value == "█":
                    self.kor[y0][x].remove((x + 1, y0))
                    self.kor[y0][x + 1].remove((x, y0))

    def __str__(self):
        N = self.N
        c = ["█" * (2 * N + 1)]
        for y in range(N):
            s = ["█"]
            for x in range(N):
                s.append("·")
                if (x+1, y) in self.kor[y][x]:
                    s.append("·")
                else:
                    s.append("█")
            s = "".join(s)
            c.append(s)
            r = ["█"]
            for x in range(N):
                if (x, y+1) in self.kor[y][x]:
                    r.append("·")
                else:
                    r.append("█")
                r.append("█")
            r = "".join(r)
            c.append(r)
        return "\n".join(c)

import sys
exec(sys.stdin.read())