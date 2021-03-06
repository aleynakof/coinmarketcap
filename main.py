import requests
import json

api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/"
                           "listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=9134ad4d-3ba1-4017-85b1-c5ec86a2a50a")
# print(api_request)
# to achieve the code in a proper format
result = json.loads(api_request.content)
# print(result)

# total count
# print(result["status"]["total_count"])

#basket = ["BTC", "LTC", "ADA"]

#print("--------")
#for i in range(10):
#    for coin in basket:
 #       if result["data"][i]["symbol"] == coin:
  #          print(result["data"][i]["symbol"])
   #         print("Price: ${0:.2f}".format(result["data"][i]["quote"]["USD"]["price"]))
    #        print("---")

# since we have multiple elements, we first need to create
# list and then set up the dictionary.
# meaning keeping dictionaries in list
basket2 = [{
    "symbol": "BTC",
    "amount": 3,
    "price": 48000
},
    {
        "symbol": "ADA",
        "amount": 300,
        "price": 1.05
    },
    {
        "symbol": "LTC",
        "amount": 48,
        "price": 185
    }]


print("---------")
total_profitloss = 0
for i in range(10):
    for coin in basket2:
        if result["data"][i]["symbol"] == coin["symbol"]:
            profitloss_per_coin = result["data"][i]["quote"]["USD"]["price"] - coin["price"]
            overall_cost = coin["amount"] * coin["price"]
            total_profitloss = total_profitloss + coin["amount"] * profitloss_per_coin

            print(result["data"][i]["symbol"])
            #buting price from basket
            print("Buying Price: ${0:.2f}".format(coin["price"]))
            #effective price from api
            print("Effective Price: ${0:.2f}".format(result["data"][i]["quote"]["USD"]["price"]))
            print("Amount: ", coin["amount"])
            print("Profit and Loss:${0:.2f}".format(profitloss_per_coin))
            print("Total Cost ${0:.2f}".format(overall_cost))
            print("---")

print(total_profitloss)