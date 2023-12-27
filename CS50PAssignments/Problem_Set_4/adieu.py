def returns_required_output():
    name_list = []
    while True:
        try:
            name = input('Name: ')
            name_list.append(name)
        except EOFError:
            break
    no_of_names = len(name_list)
    print('Adieu, adieu, to, ', end='')
    for name_ in name_list[0: no_of_names - 1]:
        print(name_ + ', ', end='')
    print('and', name_list[no_of_names - 1])


returns_required_output()
