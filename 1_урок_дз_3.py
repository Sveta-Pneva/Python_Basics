for i in range(101):
    if i == 1 or i % 10 == 1 and i > 20:
        print(i, " процент")
    elif i > 1 and i < 5 or i % 10 > 1 and i % 10 < 5 and i > 20:
        print(i, " процента")
    else:
        print(i, " процентов")