def remove_vowel(word):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    letters = list(word)
    for letter in letters:
        if letter in vowels:
            letters.remove(letter)
    out = ''
    for let in letters:
        out += let
    return (out)


def main():
    user_input = input('Please enter the word to remvove vowles from - ')
    print(remove_vowel(user_input))


if __name__ == '__main__':
    main()
