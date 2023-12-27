def converts_to_percentage(prompt):
    while True:
        fraction = input(prompt)
        x_nd_y = fraction.split('/')
        try:
            x = int(x_nd_y[0])
            y = int(x_nd_y[1])
        except ValueError:
            pass
        else:
            if y > x:
                return (x / y) * 100
            elif y == 0:
                print('Not divisible by 0')
            else:
                print('Not a fraction')


def main():
    percentage = converts_to_percentage('Fraction:')
    if percentage <= 1:
        print('E')
    elif percentage >= 99:
        print('F')
    else:
        print(f'{percentage}%')


main()
