answer = 0
num_cube = [i**3 for i in range(1, 1001, 2)]
for i in range(500):
    num = num_cube[i] + 17
    num_copy = num
    sum_num = 0
    while num != 0:
        sum_num += num % 10
        num //= 10
    if sum_num % 7 == 0:
        answer += num_copy
print(answer)