amount_due = 50
total = 0
while total < 50:
    print(f'amount due = {amount_due}')
    coin_inserted = int(input('Insert Coin: '))
    if coin_inserted == 25 or coin_inserted == 10 or coin_inserted == 5:
        amount_due -= coin_inserted
        total += coin_inserted
    else:
        print('Please enter the correct coin')
change_owed = -1 * amount_due
print(f'Change owed = {change_owed} ')
