def odd_nums(stop_value):
    stop_value -= 1
    current = -1
    while current < stop_value:
        current += 2
        yield current

num = int(input())
a = odd_nums(num)
while True:
    try:
        print(next(a))
    except:
        break