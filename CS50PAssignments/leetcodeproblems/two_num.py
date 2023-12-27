def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(calculate_sum(list1, list2))


def calculate_sum(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    list1.reverse()
    list2.reverse()
    num1 = 0
    num2 = 0
    for i in range(len1):
        num1 = num1 + (list1[i] * (10 * (len1 - i)))

    for i in range(len2):
        num2 = num2 + (list2[i] * (10 * (len2 - i)))

    return num1 + num2


if __name__ == "__main__":
    main()
