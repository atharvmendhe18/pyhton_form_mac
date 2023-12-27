import sys
import csv


def returns_no_of_dictionary_in_a_list(given_dict):
    return len(given_dict)


def read_given_file_and_return_dict(given_file):
    names_and_houses = []
    try:
        with open(given_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                names_and_houses.append(
                    {'last_first_name': row['name'], 'house': row['house']})
        return names_and_houses
    except IOError:
        print('cant read given file ')
        sys.exit()


def convert_before_to_after(before_dict):
    no_of_students = returns_no_of_dictionary_in_a_list(before_dict)
    for index in range(0, no_of_students):
        last_first = before_dict[index]['last_first_name']
        last_name, first_name = last_first.split(', ')
        before_dict[index]['First Name'] = first_name
        before_dict[index]['Last Name'] = last_name
        del before_dict[index]['last_first_name']
    return before_dict


def creat_and_save_names_in_new_file(after_dict):
    after_file_name = sys.argv[2]
    with open(after_file_name, 'w') as finalfile:
        writer = csv.DictWriter(finalfile, fieldnames=[
                                'first', 'last', 'house'])
        no_of_dict = returns_no_of_dictionary_in_a_list(after_dict)
        writer.writeheader()
        for index in range(0, no_of_dict):
            writer.writerow(
                {'first': after_dict[index]['First Name'], 'last': after_dict[index]['Last Name'], 'house': after_dict[index]['house']})


def main():
    if len(sys.argv) < 3:
        print('Too less arguments')
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many arguments")
        sys.exit()
    else:
        creat_and_save_names_in_new_file(convert_before_to_after(
            read_given_file_and_return_dict(sys.argv[1])))


main()
