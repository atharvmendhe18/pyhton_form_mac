import sys


def main():

    with open(sys.argv[1]) as file:
        count = 0
        for line in file:
            if check_if_line_is_comment(line) == True or check_if_line_is_blank(line) == True:
                pass
            else:
                count += 1

    print(count)


def check_if_line_is_comment(line):
    return line.startswith('#')


def check_if_line_is_blank(line):
    return line.isspace()


main()
