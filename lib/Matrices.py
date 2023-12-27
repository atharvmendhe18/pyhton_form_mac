def split_input(letter):
    letter = list(letter)
    return letter


def give_numbers_in_imput(list):
    res = [int(i) for i in list if i.isdigit()]
    return res


a = input('A-')
list_of_A = split_input(a)
numbers_in_A = give_numbers_in_imput(list_of_A)
print(numbers_in_A)




