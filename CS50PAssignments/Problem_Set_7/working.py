import re


def convert(s):
    time = re.search(
        r"^([1-9][0-2]?):?([0-6][0-9])? ([AP]M) to ([1-9][0-2]?):?([0-6][0-9])? ([AP]M)$", s)
    if time:

        start_time = f"{time.group(1)}:{time.group(2)} {time.group(3)}"
        end_time = f"{time.group(4)}:{time.group(5)} {time.group(6)}"

        if 'PM' in start_time:
            if time.group(2) == None:
                start_time = f"{int(time.group(1)) + 12}:00"
            else:
                start_time = f"{int(time.group(1)) + 12}:{time.group(2)}"

            if time.group(5) == None:
                end_time = f"{'{:0>2}'.format(int(time.group(4)))}:00"
            else:
                end_time = f"{'{:0>2}'.format(int(time.group(4)))}:{time.group(5)}"

        elif 'PM' in end_time:
            if time.group(5) == None:
                end_time = f"{int(time.group(4)) + 12}:00"
            else:
                end_time = f"{int(time.group(4)) + 12}:{time.group(5)}"

            if time.group(2) == None:
                start_time = f"{'{:0>2}'.format(int(time.group(1)))}:00"
            else:
                start_time = f"{'{:0>2}'.format(int(time.group(1)))}:{time.group(2)}"

        else:
            pass

    else:
        print('wopise')

    return f"{start_time} to {end_time}"


def main():
    print(convert(input('Hours: ').strip()))


if __name__ == "__main__":
    main()
