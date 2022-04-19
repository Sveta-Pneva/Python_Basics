def main(argv):
    program, *args = argv
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        lines = f.readline()
        lines = str(lines).split(',')
        if len(args) == 2:
            start = int(list(args)[0]) - 1
            end = int(list(args)[1])
            res = lines[start:end]
        elif len(args) == 1:
            start = int(list(args)[0]) - 1
            res = lines[start:]
        else:
            res = lines
    for i in res:
        print(i)

if __name__ == '__main__':
    import sys

    exit(main(sys.argv))