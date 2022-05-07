class Exception:
    def __init__(self, *args):
        self.args = args
    def checker(self):
        result = []
        for i in self.args:
            if 'str' in str(type(i)) and '.' not in i and i.isalpha() == False\
                    or 'int' in str(type(i)):
                if 'int' in str(type(int(i))) and 'float' not in str(type(i)):
                    result.append(int(i))
        return result
a = Exception(1, 2, 3.1, 0.5, '4', '4.5', 'hhh', '98')
print(a.checker())