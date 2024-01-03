import sys
import requests

currency = input().upper()
cache = {}
url = f"http://www.floatrates.com/daily/{currency}.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'usd' in data and 'eur' not in data:
        usd_rate = data['usd']['rate']
        cache = {'USD': usd_rate, 'EUR': 1}
    elif 'eur' in data and 'usd' not in data:
        eur_rate = data['eur']['rate']
        cache = {'USD': 1, 'EUR': eur_rate}
    elif 'eur' in data and 'usd' in data:
        eur_rate = data['eur']['rate']
        usd_rate = data['usd']['rate']
        cache = {'USD': usd_rate, 'EUR': eur_rate}

while True:
    try:
        currency_exchange = input()
        if not currency_exchange:
            break
        else:
            amount_money = input()
            url = f"http://www.floatrates.com/daily/{currency}.json"  # formatting matters
            r = requests.get(url)
            response_dict = r.json()
            lower = currency_exchange.lower()
            rate = response_dict[f'{lower}']['rate']
            print("Checking the cache...")
            if currency_exchange.upper() in cache:
                print("Oh! It is in the cache!")
                print(f"You received {round(float(amount_money) * cache[currency_exchange.upper()],2)} {currency_exchange.upper()}.")

            elif currency_exchange != 'USD' or currency_exchange != 'EUR':
                print("Sorry, but it is not in the cache!")
                print(f"You received {round(float(amount_money) * response_dict[f'{lower}']['rate'],2)} "
                      f"{currency_exchange.upper()}.")
                cache[currency_exchange.upper()] = rate
    except ValueError:
        break














