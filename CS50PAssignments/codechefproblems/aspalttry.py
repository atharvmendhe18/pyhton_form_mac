array_b = input("array_b").split(" ")
array_b = list(map(int, array_b))

if array_b[0] == 1:
    array_a = [1, 2]
elif array_b[0] == 0:
    array_a = [1, 1]

for i in range(1, len(array_b) - 1):
    if array_b[i] == 1:
        if array_a[i] == 1:
            array_a.append(2)
        elif array_a[i] == 2:
            array_a.append(1)
    elif array_b[i] == 0:
        if array_a[i] == 1:
            array_a.append(1)
        elif array_a[i] == 2:
            array_a.append(2)

print(array_a)

array_e = []
digits = len(array_b)
for i in range(digits):
    if i == digits - 1:
        array_e.append((int(array_a[0]) + int(array_a[digits - 1])) % 2)
    else:
        array_e.append((int(array_a[i]) + int(array_a[i + 1])) % 2)

print(array_e)
