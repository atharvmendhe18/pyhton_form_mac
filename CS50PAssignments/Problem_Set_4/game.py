import random
while True:
    try:
        level = int(input('Level: '))
    except ValueError:
        pass
    else:
        if level > 0:
            random_integer = random.randint(0, level + 1)
            while True:
                try:
                    guessed_integer = int(input('Guess: '))
                except ValueError:
                    pass
                else:
                    if random_integer == guessed_integer:
                        print('Just Right!')
                        break
                    elif random_integer > guessed_integer:
                        print('Too Small!')
                    else:
                        print('Too Large!')
        else:
            pass
