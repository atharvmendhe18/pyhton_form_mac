def is_card_no(cardno):
    lencard = len(cardno)
    if lencard == 15 or lencard == 16 or lencard == 13:
        return True
    else:
        return False


def last_no(cardno):
    return cardno % 10


def main():
    card_no = input('Number: ')
    if is_card_no(card_no):
        print('T')
    else:
        print('F')
    print(last_no(card_no))


main()
