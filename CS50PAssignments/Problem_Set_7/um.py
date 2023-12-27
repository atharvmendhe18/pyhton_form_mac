import re


def count(s):
    if s[0:2] == 'um':
        count = 1
    else:
        count = 0
    umhs = re.findall(r"[ ,?./:]um[ ,?.]?", s)
    if umhs:
        return len(umhs) + count
    else:
        return 'wopise'


def main():
    print(count(input('Input: ').lower()))


if __name__ == "__main__":
    main()
