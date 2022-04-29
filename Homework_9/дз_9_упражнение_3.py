class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.result = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        res = self.name + ' ' + self.surname
        return res
    def get_total_income(self):
        return sum(self.result.values())

a = Position('Майя', 'Кузнецова', 'Выпускающий редактор', 700000, 3900)
print(a.get_full_name())
print(a.get_total_income())