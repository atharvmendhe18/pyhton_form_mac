def convert_camelcase_to_snakecase(name_in_camel_case):
    for letter in name_in_camel_case:
        if letter.isupper():
            lower_letter = letter.lower()
            name_in_snake_case = name_in_camel_case.replace(
                letter, "_" + lower_letter)
    return name_in_snake_case


def main():
    user_input = input('Camel case: ')
    print(convert_camelcase_to_snakecase(user_input))


main()
