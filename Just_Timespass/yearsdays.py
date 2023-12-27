
no_of_days = int(input('Please enter the no of days- '))
years = no_of_days // 365
months = (no_of_days % 365) // 30
weeks = ((no_of_days % 365) % 30) // 7
days = ((no_of_days % 365) % 30) % 7
print(f'{years}years {months}months {weeks}weeks {days}days')




