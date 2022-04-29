class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f'{self.title} - просто рисую'

class Pen(Stationery):
    def draw(self):
        return f'{self.title} - ручка'

class Pencil(Stationery):
    def draw(self):
        return f'{self.title} - карандаш'

class Handle(Stationery):
    def draw(self):
        return f'{self.title} - маркер'

a = Stationery('что-то')
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(a.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())