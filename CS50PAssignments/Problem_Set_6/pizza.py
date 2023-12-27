from tabulate import tabulate
import sys
import csv


def return_a_dict_of_data():
    menu = []
    if len(sys.argv) != 2:
        sys.exit()
    else:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(
                    {'Regular Pizza': row['Regular Pizza'], 'Samll': row['Small'], 'Large': row['Large']})
        return menu


def convert_to_table(menu):
    print(tabulate(menu, headers='keys', tablefmt='grid'))


def main():
    convert_to_table(return_a_dict_of_data())


main()
