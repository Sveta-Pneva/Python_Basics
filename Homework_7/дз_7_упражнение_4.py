import os

a = []
b = {}
def file_sizes(path):
    files_stat = [0, 0, 0]
    for i_elem in os.listdir(path):
        if os.path.isfile(os.path.abspath(os.path.join(path, i_elem))):
            file_path = os.path.abspath(os.path.join(path, i_elem))
            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size
            a.append(file_size)
            files_stat[1] += 1
        else:
            result = file_sizes(os.path.abspath(os.path.join(path, i_elem)))
            files_stat[0] += result[0]
            files_stat[1] += result[1]
            files_stat[2] += 1
        for i in a:
            j = 10
            while j < i:
                j *= 10
            if j in b:
                 b[j] += 1
            else:
                 b[j] = 1
            a.clear()
    return files_stat



path = os.path.abspath(os.path.join('my_project'))
result = file_sizes(path)
print(b)