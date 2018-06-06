import json
from urllib.request import urlopen
#
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as r:
    #     source = resp.read()
    # with open('quote.json','r') as r:
    source = r.read()
data = json.loads(source)
# print(json.dumps(data,indent =2))
# print(len(data["list"]["resources"]))

usd_rates = {}

for item in data["list"]["resources"]:
    # print(item)
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    print(name, price)
    # usd_rates[name] = price


# print(50 * float(usd_rates['USD/INR']))
