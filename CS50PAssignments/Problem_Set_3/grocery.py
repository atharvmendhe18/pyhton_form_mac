
def output_list():
    groceries = []
    while True:
        try:
            new_item = input('')
            groceries.append(new_item)
        except EOFError:
            break
    return groceries


def main():
    sorted_list = output_list()
    sorted_list.sort()
    for item in sorted_list:
        no_of_times = sorted_list.count(item)
        for _ in range(no_of_times - 1):
            sorted_list.remove(item)
        print(no_of_times, item.upper())


main()
