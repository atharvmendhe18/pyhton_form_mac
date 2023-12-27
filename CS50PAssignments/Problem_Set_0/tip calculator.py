tot_bill = input('How much is your bill - ')
perce_tip = input('How much percentage of tip would you like to give? ')


def tip_calculator(bill, percent_tip):
    bill = bill.split('$')
    bill_float = float(bill[1])
    percent_tip = percent_tip.split('%')
    percent_tip_float = float(percent_tip[0])

    return (bill_float * (percent_tip_float / 100))


print(f'Tip to be given is {tip_calculator(tot_bill, perce_tip)}')
