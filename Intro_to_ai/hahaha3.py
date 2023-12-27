lst = [1, 2, 3, 1, 2, 4]
lst.sort
my_dict = {}

for i in set(lst):
    count = 0
    for j in lst:
        if i == j:
            count += 1

    my_dict[i] = count

print(my_dict)
