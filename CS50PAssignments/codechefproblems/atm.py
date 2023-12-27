import sys


def main():
    test_cases = int(input("No of test Cases: "))
    for _ in range(test_cases):
        atm()
        print()


def atm():
    no_of_people, total_money = input(
        "'No of people  Total amount of money' seperated by space: ").split(" ")
    money_asked = input("Money needed sperated by a space: ").split(" ")
    if int(no_of_people) == 0 or int(total_money) == 0 or len(money_asked) == 0:
        sys.exit()
    for i in money_asked:
        if int(i) <= int(total_money):
            print("1", end=" ")
            total_money = int(total_money) - int(i)
        else:
            print("0", end=" ")


if __name__ == "__main__":
    main()
