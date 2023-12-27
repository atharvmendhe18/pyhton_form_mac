def main():
    iterations = int(input("Please enter the no of test cases: "))

    for _ in range(iterations):
        len_word = input("length of the word: ")
        user_word = input("Please enter the word:")
        if difficult_to_pronounce(user_word):
            print("NO")
        else:
            print("YES")


def difficult_to_pronounce(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    c = 0
    max_c = 0
    for i in word:
        if i in vowels:
            if c > max_c:
                max_c = c
            c = 0
        else:
            c = c + 1
            max_c = c
    if max_c >= 4:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
