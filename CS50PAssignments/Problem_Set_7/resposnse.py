from validator_collection import checkers


email_address = input('What is your E-Mail address: ')

if checkers.is_email(email_address):
    print('Valid')
else:
    print('Invalid')
