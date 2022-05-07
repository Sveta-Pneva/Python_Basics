class ZeroDivisionError:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    @staticmethod
    def zero_division(dividend, divisor):
        try:
            return dividend / divisor
        except:
            return f"Деление на ноль - ошибка: divisor = {divisor}"


print(ZeroDivisionError.zero_division(48, 23))
print(ZeroDivisionError.zero_division(20, 0))
print(ZeroDivisionError.zero_division(2, 0.08))