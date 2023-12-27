def convert_US_dates_to_normal_dates():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        date = input('Date: ')

        try:
            _ = int(date[0])
        except ValueError:
            list = date.split(' ')
            month = list[0]
            month_in_int = months.index(month) + 1
            day = list[1]
            day = int(day[0])
            year = list[2]
            if month_in_int <= 12 and day <= 31:
                converted_date = f'{year}-{month_in_int:02}-{day:02}'
                return converted_date
            else:
                pass

        else:
            try:
                list_1 = date.split('/')
                mont_h = int(list_1[0])
                da_y = int(list_1[1])
                yea_r = list_1[2]
                if mont_h <= 12 and da_y <= 31:
                    converted_dat_e = f'{yea_r}-{mont_h:02}-{da_y:02}'
                    return converted_dat_e
                else:
                    pass
            except ValueError:
                pass


print(convert_US_dates_to_normal_dates())
