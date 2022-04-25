def type_logger(func):
    def type_args(*args):
        res_type_logger = {}
        res_calc_cube = {}
        for i in args:
            res_type_logger[i] = type(i)
            res_calc_cube[i] = func(i)
        print(res_type_logger)
        print(res_calc_cube)
    return type_args

@type_logger
def calc_cube(*args):
    for i in args:
        i = int(i)
        return i ** 3

calc_cube(2, 7)