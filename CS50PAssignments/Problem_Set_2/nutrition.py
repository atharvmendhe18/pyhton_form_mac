def calculate_fruit_calores(fruit):
    fruit_calories = {
        'apple': 30,
        'avocado': 50,
        'banana': 110,
        'Cantaloupe': 50,
        'grapefruit': 60,
        'grapes': 90,
        'Honeydew Melon': 50,
        'kiwifruit': 50,
        'lemon': 15,
        'lime': 20,
        'nectarine': 60,
        'orange': 80,
        'peach': 60,
        'pear': 100,
        'pineapple': 50,
        'plums': 70,
        'strawberries': 50,
        'sweet cherries': 100,
        'tangerine': 50,
        'watermelon': 80,

    }
    if fruit in fruit_calories:
        return fruit_calories[fruit]
    else:
        return quit()


def main():
    user_input_fruit = input('Item: ').lower()
    print('calories= ', calculate_fruit_calores(user_input_fruit))


main()
