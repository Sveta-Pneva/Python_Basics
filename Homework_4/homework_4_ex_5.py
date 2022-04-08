import homework_4_ex_2 as hw
def main(argv):
    n = ""
    n += argv[1]
    n = hw.currency_rates(n)
    print(n)

if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
