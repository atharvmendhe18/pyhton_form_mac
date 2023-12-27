
def main():
    for _ in range(int(input("testcases "))):
        if check_b():
            print("YES")
        else:
            print("NO")


def check_b():
    digits = int(input("digits "))
    array_b = input("array b ").split(" ")
    array_a = []
    for j in range(digits):
        array_b[j] = int(array_b[j])

    for _ in range(digits):
        array_a.append("1")
    array_d = []
    array_e = []

    for i in range(digits):
        if i == digits - 1:
            array_d.append((int(array_a[0]) + int(array_a[digits - 1])) % 2)
        else:
            array_d.append((int(array_a[i]) + int(array_a[i + 1])) % 2)

    if array_d == array_b:
        return True

    for k in range(digits):
        for i in range(digits):
            for j in range(digits):
                if array_a[i] != array_a[j]:
                    # check array_a == array_b
                    array_c = []
                    for i in range(digits):
                        if i == digits - 1:
                            array_c.append(
                                (int(array_a[0]) + int(array_a[digits - 1])) % 2)
                        else:
                            array_c.append(
                                (int(array_a[i]) + int(array_a[i + 1])) % 2)

                    if array_c == array_b:
                        return True

                    temp = array_a[j]
                    array_a[j] = array_a[i]
                    array_a[i] = temp

        array_a[k] = "2"

    for i in range(digits):
        if i == digits - 1:
            array_e.append((int(array_a[0]) + int(array_a[digits - 1])) % 2)
        else:
            array_e.append((int(array_a[i]) + int(array_a[i + 1])) % 2)

    if array_e == array_b:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
