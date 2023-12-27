def check_if_two_letters_at_start(no_plate):
    characters_to_check = no_plate[0:2]
    if characters_to_check.isalpha():
        return True
    else:
        return False


def no_whitespace_random_characters(no_plate):
    if no_plate.isalnum():
        return True
    else:
        return False


def max_6_min_2_char(no_plate):
    if len(no_plate) > 1 and len(no_plate) < 7:
        return True
    else:
        return False


def is_no_in_middle(no_plate):
    for no in no_plate:
        if no.isdigit():
            index = no_plate.find(no)
            break
    remaining_no_plate = no_plate[index:]
    for alp in remaining_no_plate:
        if alp.isalpha():
            return False
        else:
            return True


def is_first_no_zero(no_plate):
    for no in no_plate:
        if no.isdigit():
            index = no_plate.find(no)
            break
    first_num = no_plate[index]
    if first_num == '0':
        return False
    else:
        return True


def is_valid(no_plate):
    if check_if_two_letters_at_start(no_plate) and no_whitespace_random_characters(no_plate) and max_6_min_2_char(no_plate) and is_no_in_middle(no_plate) and is_first_no_zero(no_plate):
        return True
    else:
        return False


def main():
    user_input = input('Number Plate - ')
    if is_valid(user_input):
        print("Valid")
    else:
        print('Not Valid')


if __name__ == '__main__':
    main()
