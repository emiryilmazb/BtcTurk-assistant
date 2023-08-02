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

apiKey = "ade38ced-11aa-41e5-8710-c2ac3da492c9"
apiSecret = "vnh0AjNTI3E6jNyuEgqbCDpFfl5MsiXe"

apiSecret = base64.b64decode(apiSecret)
stamp = str(int(time.time())*1000)
data = "{}{}".format(apiKey, stamp).encode('utf-8')
signature = hmac.new(apiSecret, data, hashlib.sha256).digest()
signature = base64.b64encode(signature)


headers= {
  "X-PCK": apiKey,
  "X-Stamp": stamp,
  "X-Signature": signature,
  "Content-Type": "application/json"
}


my_client = Client(api_key=apiKey, api_secret="vnh0AjNTI3E6jNyuEgqbCDpFfl5MsiXe")
time = my_client.get_server_time()
balance = my_client.get_account_balance()
# print(time["serverTime2"])


balance_try = balance[0]["balance"]
balance_btc = balance[1]["balance"]
balance_atom = balance[27]["balance"]
balance_eth = balance[34]["balance"]

btctry = my_client.tick()[0]["last"]
ethtry = my_client.tick()[1]["last"]
atomtry = my_client.tick()[19]["last"]

btc_amount = 2500
eth_amount = 1875
atom_amount = 625


result_btc = float(balance_btc) * btctry
result_atom = float(balance_atom) * atomtry
result_eth = float(balance_eth) * ethtry

# print(result_btc)
# print(result_atom)
# print(result_eth)

total_tl_amount = result_atom + result_btc + result_eth + float(balance_try)

print(total_tl_amount)
print(result_btc)
# print(balance_btc)
# print(balance_atom)
# print(balance_eth)

# for item in balance:
#     if float(item["balance"]) > 0:
#         print(item)

# for item in my_client.tick():
#     if item["pair"] == "BTCTRY":
#         print(item["last"])
# c = 0
# for item in my_client.tick():
#     if item["pair"] == "ATOMTRY":
#         print(item)
#         print
#         break
#     c +=1

# c = 0
# for item in balance:
#     if item["asset"] == "ETH":
#         print(item)
#         print(c)
#         break
#     c +=1

