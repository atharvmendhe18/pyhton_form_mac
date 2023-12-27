import requests
import sys
import json

response = requests.get(' https://api.coindesk.com/v1/bpi/currentprice.json')
o = response.json()
usd_rate = o["bpi"]["USD"]["rate"]
usd_rate = float(usd_rate.replace(',', ''))


if len(sys.argv) == 1:
    print('Missing commnad line argument')
    sys.exit()
else:
    try:
        user_input = int(sys.argv[1])
    except ValueError:
        print('Command line argument not a number.')
        sys.exit()
    else:
        print('{:,}'.format(user_input * usd_rate))
