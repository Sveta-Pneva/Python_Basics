def main(argv):
    sale = argv
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(str(sale) + ',')
    return 'bakery.csv'

if __name__ == '__main__':
    import sys

    exit(main(str((sys.argv)[1])))