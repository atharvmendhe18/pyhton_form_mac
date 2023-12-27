my_dictv = {}

for i in range(3):
    key = input("eneter key: ")
    val = int(input("enter value: "))
    my_dictv[i] = val

avg = 0

for i in my_dictv:
    avg += my_dictv[i]

print(avg / len(my_dictv))
