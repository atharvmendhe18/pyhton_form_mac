def convert(time):
    time = time.split(':')
    hour = time[0]
    min = int(time[1]) / 60
    min = str(min).split('.')
    min = min[1]
    converted_time = f'{hour}.{min}'
    return float(converted_time)


def main():
    user_time = input('Please enter time in ##:## format- ')
    print(convert(user_time))
    if convert(user_time) > 7.00 and convert(user_time) < 8.00:
        print('Breakfast')
    elif convert(user_time) > 12.00 and convert(user_time) < 13.00:
        print('Lunch time')
    elif convert(user_time) > 18.00 and convert(user_time) < 19.00:
        print('Dinner time')


main()
