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

btc_amount = 2500
eth_amount = 1875
atom_amount = 625
desired_currency = "TRY"  # you can choose your desired currency "USD" or "TRY"


with open("secret.txt") as f:
    contents = f.read()
    apiKey = contents.split("\n")[0]  # the api key that you took from btcturk API goes to first line of the secret.txt file
    apiSecret = contents.split("\n")[1].strip()  # the api secret goes to second line of the secret.txt file

my_client = Client(api_key=apiKey, api_secret=apiSecret)
time = my_client.get_server_time()
balance = my_client.get_account_balance()
newbalance = []
mycurrency = []

for item in balance:
    if float(item["balance"]) > 0:
        newbalance.append(item)
        mycurrency.append(item["asset"])
# print(mycurrency)

for item in my_client.tick():
    # if item["pair"] + desired_currency in mycurrency:
    if item["pair"].replace(desired_currency,"") in mycurrency:
        # print(item)
        pass
print(newbalance)


balance_try = balance[0]["balance"]
balance_btc = balance[1]["balance"]
balance_atom = balance[27]["balance"]
balance_eth = balance[34]["balance"]

btctry = my_client.tick()[0]["last"]
ethtry = my_client.tick()[1]["last"]
atomtry = my_client.tick()[19]["last"]


result_btc = float(balance_btc) * btctry
result_atom = float(balance_atom) * atomtry
result_eth = float(balance_eth) * ethtry

# print(result_btc)
# print(result_atom)
# print(result_eth)

total_tl_amount = result_atom + result_btc + result_eth + float(balance_try)

# print(total_tl_amount)
