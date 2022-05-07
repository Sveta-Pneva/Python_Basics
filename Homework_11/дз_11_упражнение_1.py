class Date:
    def __init__(self, date):
        self.date = str(date)
    @classmethod
    def new_date(cls, date):
        if len(date) == 10:
            day = int(date[:2])
            month = int(date[3:5])
            year = int(date[6:])
        else:
            day = int(date[:2])
            month = int(date[2:4])
            year = int(date[4:])
        return day, month, year
    @staticmethod
    def valid(date):
        day = Date.new_date(date)[0]
        month = Date.new_date(date)[1]
        year = Date.new_date(date)[2]
        res = ''
        if 1 > day or day > 31:
            res += f'false day:{day}\n'
        if 1 > month or month > 12:
            res += f'false month:{month}\n'
        if 1 > year:
            res += f'false year:{year}\n'
        if len(res) == 0:
            res = 'true value\n'
        res = res[:len(res) - 1]
        return res

print(Date.new_date('12345555'))
print(Date.valid('12340000'))
print(Date.valid('16.04.2007'))