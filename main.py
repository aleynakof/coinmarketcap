import requests
import json
from tkinter import *


def rgb_color(rgb):
    return '#%02x%02x%02x' % rgb


def center_window(w=300, h=200):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


# mainloopun altındaki kodlar mainloopla
# gelen ekranı kapatmadan çalışmaz

def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/"
                               "listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=9134ad4d-3ba1-4017-85b1"
                               "-c5ec86a2a50a")
    # print(api_request)
    # to achieve the code in a proper format
    result = json.loads(api_request.content)
    # print(result)

    # total count
    # print(result["status"]["total_count"])

    # basket = ["BTC", "LTC", "ADA"]

    # print("--------")
    # for i in range(10):
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

    satir_no = 1

    for i in range(10):
        for coin in basket2:
            if result["data"][i]["symbol"] == coin["symbol"]:
                profitloss_per_coin = result["data"][i]["quote"]["USD"]["price"] - coin["price"]
                overall_cost = coin["amount"] * coin["price"]
                total_profitloss = total_profitloss + coin["amount"] * profitloss_per_coin

                print(result["data"][i]["symbol"])
                # buting price from basket
                print("Buying Price: ${0:.2f}".format(coin["price"]))
                # effective price from api
                print("Effective Price: ${0:.2f}".format(result["data"][i]["quote"]["USD"]["price"]))
                print("Amount: ", coin["amount"])
                print("Profit and Loss:${0:.2f}".format(profitloss_per_coin))
                print("Total Cost ${0:.2f}".format(overall_cost))
                print("---")

                name = Label(window, text=coin["sembol"], bg=rgb_color((0, 0, 128)), fg='white')
                name.grid(row=satir_no, column=0)

                price = Label(window, text="${0:.2f}".format(coin["fiyat"]), fg=rgb_color((0, 0, 128)), bg='white')
                price.grid(row=satir_no, column=1)

                no_coins = Label(window, text=coin["miktar"], bg=rgb_color((0, 0, 128)), fg='white')
                no_coins.grid(row=satir_no, column=2)

                amount_paid = Label(window, text="${0:.2f}".format(overall_cost), fg=rgb_color((0, 0, 128)),
                                    bg='white')
                amount_paid.grid(row=satir_no, column=3)

                current_val = Label(window, text="${0:.2f}".format(result["data"][i]["quote"]["USD"]["price"]),
                                    bg=rgb_color((0, 0, 128)), fg='white')
                current_val.grid(row=satir_no, column=4)

                pl_coin = Label(window, text="${0:.2f}".format(profitloss_per_coin), fg=rgb_color((0, 0, 128)),
                                bg='white')
                pl_coin.grid(row=satir_no, column=5)

                total_pl = Label(window, text="${0:.2f}".format(total_profitloss), bg=rgb_color((0, 0, 128)),
                                 fg='white')
                total_pl.grid(row=satir_no, column=6)

    print(total_profitloss)


window = Tk()
window.title('My Coin Portfolio')
window.geometry('600x200')
center_window(700, 200)

name = Label(window, text='Coin Name', bg=rgb_color((0, 0, 128)), fg='white')
name.grid(row=0, column=0)

price = Label(window, text='Price', fg=rgb_color((0, 0, 128)), bg='white')
price.grid(row=0, column=1)

no_coins = Label(window, text='Coin Owned', bg=rgb_color((0, 0, 128)), fg='white')
no_coins.grid(row=0, column=2)

amount_paid = Label(window, text='Total Amount Paid', fg=rgb_color((0, 0, 128)), bg='white')
amount_paid.grid(row=0, column=3)

current_val = Label(window, text='Current Value', bg=rgb_color((0, 0, 128)), fg='white')
current_val.grid(row=0, column=4)

pl_coin = Label(window, text='Profit Loss Per Coin', fg=rgb_color((0, 0, 128)), bg='white')
pl_coin.grid(row=0, column=5)

total_pl = Label(window, text='Total Profit Loss with Coin', bg=rgb_color((0, 0, 128)), fg='white')
total_pl.grid(row=0, column=6)

window.mainloop()
