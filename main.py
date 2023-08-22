
# you should keep that in mind when you create your own api, it requires your public API which changes 
# under some conditions, if it changes you'll get Authentication Error. 


import time
import hmac
import base64
import hashlib
import json
import btcturk_api.client
import btcturk_api.constants
import btcturk_api.exceptions
import btcturk_api.properties
from btcturk_api.client import Client

# Settings
btc_amount = 2500
eth_amount = 1875
atom_amount = 625
desired_currency = "TRY"  # you can choose your desired currency with their short version like "USD" or "TRY".
secretfile = "secret.txt" # the file should contain api keys

# reads api keys from folder
with open(secretfile) as f:
    contents = f.read()
    apiKey = contents.split("\n")[0]  # the api key that you took from btcturk API goes to first line of the secret.txt file
    apiSecret = contents.split("\n")[1].strip()  # the api secret goes to second line of the secret.txt file

# calls btcturk_api and implement with api keys
my_client = Client(api_key=apiKey, api_secret=apiSecret)
time = my_client.get_server_time()
balance = my_client.get_account_balance()
my_wallet = []
my_currency = []

# gets 
for item in balance:
    if float(item["balance"]) > 0:
        my_wallet.append(item)
        my_currency.append(item["asset"])


btc_price = my_client.tick('BTC_TRY')
# print(btc_price)
# print(my_wallet)
for item in my_currency:
    for item_value in my_client.tick(f"{item}_{desired_currency}"):
        print(item_value)



    # for currency in my_currency:
    #     if item["pair"].replace(desired_currency,"") == currency:
    #         print(currency, my_currency)











            # if currency == my_currency["asset"]:
            #     print(my_currency["asset"])


            
    # if item["pair"] + desired_currency in my_currency:
    # if item["pair"].replace(desired_currency,"") in my_currency:
    #     print(item)













# print(result_btc)
# print(result_atom)
# print(result_eth)


# print(total_tl_amount)




# balance_try = balance[0]["balance"]
# balance_btc = balance[1]["balance"]
# balance_atom = balance[27]["balance"]
# balance_eth = balance[34]["balance"]

# btctry = my_client.tick()[0]["last"]
# ethtry = my_client.tick()[1]["last"]
# atomtry = my_client.tick()[19]["last"]


# result_btc = float(balance_btc) * btctry
# result_atom = float(balance_atom) * atomtry
# result_eth = float(balance_eth) * ethtry

# total_tl_amount = result_atom + result_btc + result_eth + float(balance_try)
