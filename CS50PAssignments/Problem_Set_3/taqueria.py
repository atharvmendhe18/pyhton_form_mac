def return_price(item):
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    if item in menu:
        return menu[item]
    else:
        return 0


def main():
    total = 0.00
    while True:
        user_item = input('Item: ')
        print('Price =', return_price(user_item))
        total += return_price(user_item)
        print(f'Total = {total}')


main()
