class Cell:
    def __init__(self, num):
        self.num = int(num)
    def __add__(self, other):
        return Cell(self.num + other.num)
    def __mul__(self, other):
        return Cell(self.num * other.num)
    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            return ValueError
    def __truediv__(self, other):
        return Cell(self.num // other.num)
    def make_order(self, num_of_row):
        self.num_of_row = num_of_row
        result = ""
        numer = self.num
        for i in range(numer // num_of_row + 1):
            if numer < num_of_row:
                result += "*" * numer + "\n"
                break
            else:
                numer -= num_of_row
                result += "*" * num_of_row + "\n"
        result = result[:len(result)-1]
        print(result)
a = Cell(18)
a.make_order(4)
b = Cell(21)
b.make_order(6)
c = a + b
c.make_order(10)
m = a * b
m.make_order(24)
n = b - a
n.make_order(3)
v = a - b
print(v)
l = m / n
l.make_order(24)