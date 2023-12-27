def main():
    testcases = int(input(""))

    for _ in range(testcases):
        digits = int(input(""))
        convert_to_binary(digits)


def is_even(digits):
    if digits % 2 == 0:
        return True
    else:
        return False


def convert_to_binary(digits):
    if is_even(digits) and digits > 3:
        print("1" + "0"*(digits - 2) + "1")
    else:
        print("0"*(int((digits-1)/2)) + "1" + "0"*(int((digits-1)/2)))


if __name__ == "__main__":
    main()
