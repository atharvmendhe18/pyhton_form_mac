def main():
    test_cases = int(input(""))

    for _ in range(test_cases):
        convert_to_binary()


def convert_to_binary():
    digits = int(input(""))
    my_array = []
    my_final_array = []
    for _ in range(digits):
        my_array.append("0")

    for k in range(digits):
        my_array[k] = "1"
        for i in range(digits):
            for j in range(digits):
                if my_array[i] != my_array[j]:
                    zero_one = 0
                    one_zero = 0
                    temp = my_array[j]
                    my_array[j] = my_array[i]
                    my_array[i] = temp
                    print(my_array)
                    # checking if 01 = 10
                    for l in range(digits - 1):
                        for m in range(l + 1, digits):
                            if my_array[l] + my_array[m] == "10":
                                one_zero += 1
                            elif my_array[l] + my_array[m] == "01":
                                zero_one += 1
                    if zero_one == one_zero and zero_one != 0 and one_zero != 0:
                        if f"{my_array}" not in my_final_array:
                            my_final_array.append(f"{my_array}")
                    else:
                        pass

    for i in my_final_array:
        for j in range(2, digits*5, 5):
            print(i[j], end="")
        print()


if __name__ == "__main__":
    main()
