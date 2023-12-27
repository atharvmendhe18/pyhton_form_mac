import random


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer():
    score = 0

    for __ in range(0, 10):
        no1 = random.randint(0, 10)
        no2 = random.randint(0, 10)
        attempts = 0
        while attempts <= 3:
            print(no1, '+', no2, ' = ', end='')
            ans = no1 + no2
            try:
                user_ans = int(input(''))
            except ValueError:
                print('EEE')
            else:
                if user_ans == ans:
                    score += 1
                    attempts = 4
                else:
                    attempts += 1
                    print('EEE')
            if attempts == 3:
                print(f'Answer = {ans}')

    print(score)


def main():
    get_level()
    generate_integer()


main()
