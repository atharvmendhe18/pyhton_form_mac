import re
import sys


def validate(ip):
    value = re.match(
        r"([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)", ip)
    for no in range(1, 5):
        if int(value.group(no)) in range(0, 225):
            pass
        else:
            return False
    return True


def main():
    print(validate(sys.argv[1]))


main()
