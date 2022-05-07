class Stock:
    def add_office_equipment(self, numer):
        res = {'printer': [], 'scanner': [], 'copier': [], 'other': []}
        for i in range(numer):
            try:
                name = input('name: ')
                model = input('model: ')
                num = int(input('num: '))
            except ValueError:
                return 'ошибка!!! неправильно введены данные'
            if 'print' in name or 'принт' in name:
                res['printer'].append([name, model, num])
            elif 'scan' in name or 'скан' in name:
                res['scanner'].append([name, model, num])
            elif 'cop' in name or 'ксер' in name or 'коп' in name:
                res['copier'].append([name, model, num])
            else:
                res['other'].append([name, model, num])
        return res

class Office_equipment:
    def __init__(self, name, model, num):
        self.name = name
        self.model = model
        self.num = int(num)
    def info(self):
        return f'name - {self.name}\n' \
               f'model - {self.model}\n' \
               f'how many: {self.num}'

class Printer(Office_equipment):
    def __init__(self, color_print, name, model, num):
        super().__init__(name, model, num)
        self.color_print = color_print
    def info_color(self):
        return f'model - {self.model}\ncolor - {self.color_print}'

class Scanner(Office_equipment):
    def __init__(self, x, y, name, model, num):
        super().__init__(name, model, num)
        self.x = int(x)
        self.y = int(y)
    def scan_resolution(self):
        return f'model - {self.model}\nmax scan resolution: {self.x}x{self.y} dpi'

class Copier(Office_equipment):
    def __init__(self, mfp, name, model, num):
        super().__init__(name, model, num)
        self.mfp = mfp
    def type_of_MFP(self):
        return f'model - {self.model}\nMFP - {self.mfp}'

a = Office_equipment('printer', 'adf89_ppp', 7)
print(a.info())
b = Printer('colored', 'printer', 'adf89_ppp', 7)
print(b.info_color())
c = Scanner(120, 240, 'scanner', 'pl_485_wq', 50)
print(c.scan_resolution())
k = Copier('laser', 'copier', 'la_348_co', 3)
print(k.type_of_MFP())

d = Stock()
d = d.add_office_equipment(3)
print(d)
