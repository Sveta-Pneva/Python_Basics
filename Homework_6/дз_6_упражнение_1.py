FILENAME = "nginx_logs.txt"
with open(FILENAME, 'r', encoding="utf-8") as file:
    line = file.readline()
    res = []
    while line:
        a = line.split(" ")
        res.append((a[0], str(a[5])[1:], a[6]))
        print(a)
        print(line)
        line = file.readline()
print(res[:10])

