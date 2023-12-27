height = int(input('Please enter the required height- '))
for i in range(height + 1):
    print(" "*(height - i) + "#"*i + " " + "#"*i)
print('done')
