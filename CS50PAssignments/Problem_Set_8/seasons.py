from datetime import date
import re
import sys
from num2words import num2words


def get_bitrhday():
    current_year = date.today().year
    birthdate = input('Date of birth: ')
    value = re.match(
        r"([0-2][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])", birthdate)
    if value and int(value[1]) <= current_year:
        return (int(value[1]), int(value[2]), int(value[3]))
    else:
        print('Invalid Birthdate')
        sys.exit()


def convert_to_mintues(date_tuple):
    year, month, date_ = date_tuple
    print(year)
    start_date = date(year, month, date_)
    today_date = date.today()

    diff_in_sec = (today_date - start_date).total_seconds()
    diff_in_min = diff_in_sec / 60
    return diff_in_min


def convert_min_to_words(miniutes):
    return num2words(miniutes)


def main():
    print(f"{convert_min_to_words(convert_to_mintues(get_bitrhday()))} miniutes")


if __name__ == "__main__":
    main()
