numbers = [10, 20, 39, 30, 76, 56, 20, 10, 55, 1066]
numbers.sort()
for no in numbers:
    no_of_times = numbers.count(no)
    if no_of_times > 1:
        numbers.remove(no)
print(numbers)
x = 0
for no1 in numbers:
    largestno = x
    if no1 > largestno:
        largestno = no1
print(largestno)
print()
