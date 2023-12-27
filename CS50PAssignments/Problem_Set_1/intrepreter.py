user_in = input('Expression: ').split(' ')
x = int(user_in[0])
y = int(user_in[2])
operator = user_in[1]

if operator == '+':
    print(x + y)
elif operator == '-':
    print(x - y)
elif operator == '*':
    print(x * y)
elif operator == '/':
    print(x / y)
