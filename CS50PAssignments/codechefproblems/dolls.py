def main():
    for _ in range(int(input(""))):
        stolen_doll()


def stolen_doll():
    no_of_dolls = int(input(""))
    dolls_array = []
    for _ in range(no_of_dolls):
        dolls_array.append(int(input("")))

    dolls_array.sort()

    for i in range(0, no_of_dolls, 2):
        try:
            if dolls_array[i] != dolls_array[i + 1]:
                print(f"{dolls_array[i]}")
                break
        except IndexError:
            print(dolls_array[len(dolls_array) - 1])


if __name__ == "__main__":
    main()
