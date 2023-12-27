import sys


def validate(ip):
    nos = ip.split('.')
    if len(nos) == 4:
        for no in nos:
            if int(no) in range(0, 226):
                pass
            else:
                return 'invalid'
        return 'Valid'
    else:
        return 'invalid'


def main():
    print(validate(sys.argv[1]))


if __name__ == '__main__':
    main()
