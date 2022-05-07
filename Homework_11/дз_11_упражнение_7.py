class Complex_Num:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x} + {self.y} * i'

    def __add__(self, other):
        return f'сложение: {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        return f'умножение: {self.x * other.x - (self.y * other.y)} + {self.y * other.x} * i'


a = Complex_Num(1, -2)
b = Complex_Num(3, 4)
print(a + b)
print(a * b)
print(a)