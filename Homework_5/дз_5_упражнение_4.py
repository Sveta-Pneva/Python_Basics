src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
last_num = src[0]
for i in src:
    if i > last_num:
        result.append(i)
    last_num = i
print(result)