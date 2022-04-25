def val_checker(callback):
    def _val_checker(func):
        def checker(*vals):
            for val in vals:
                if callback(val):
                    print(func(val))
                else:
                    print(f'ValueError: wrong val {val}')
        return checker
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(*args):
    for i in args:
        i = int(i)
        return i ** 3

a = calc_cube(-6, 9, 0, 47)
