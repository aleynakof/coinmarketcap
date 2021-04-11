import requests
import json
from tkinter import *
import sqlite3

con = sqlite3.connect('coin.db')
cursor = con.cursor()

#table_drop
cursor.execute("DROP TABLE coin")
con.commit()

# tabloyu oluşturuyoruz
# tabloyu oluşturduğumdan id unique olmayacak. Bu yüzden hata
# o yüzden başlamadan tabloyu düşür
cursor.execute('CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT,amount INTEGER, price REAL)')
con.commit()

cursor.execute("insert into coin values(1,'BTC',3,48000)")
con.commit()

cursor.execute("insert into coin values(?,?,?,?)", (2, 'ADA', 5, 52000))
con.commit()


def tl_formatla(para):
    # dolar formatında yazmak istersek binlik =, ve ondalik=.
    # olmalı. Bunları parametrik de verebiliriz.
    binlik = ","
    ondalik = "."

    currency = "{:,.2f}".format(para)

    if binlik == ".":
        main, fractional = currency.split('.')[0], currency.split('.')[1]

        new_main = main.replace(',', '.')
        currency = '$' + new_main + ondalik + fractional
    else:
        currency = '$' + currency
    return currency


def rgb_color(rgb):
    return '#%02x%02x%02x' % rgb


def font_color_pl(para):
    if para > 0:
        return "green"
    elif para == 0:
        return "grey"
    else:
        return "red"


def center_window(w=300, h=200):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency"
                               "/listings/latest?start=1&limit=10&convert=USD&"
                               "CMC_PRO_API_KEY=f1e4d2c9-ca98-4890-8b29-70ee91a81a86")

    result = json.loads(api_request.content)

    # print(result)

    # total count
    # print("Total count:", result["status"]["total_count"])

    sepet = [
        {
            "sembol": "BTC",
            "miktar": 3,
            "fiyat": 48000
        },
        {
            "sembol": "ADA",
            "miktar": 300,
            "fiyat": 1.05
        },
        {
            "sembol": "LTC",
            "miktar": 48,
            "fiyat": 185
        }

    ]

    # print('----------------------')

    portfoy_karzarar = 0

    satir_no = 1
    all_amount_paid = 0

    for i in range(10):
        for coin in sepet:
            if result["data"][i]["symbol"] == coin["sembol"]:
                coin_basina_karzarar = result["data"][i]["quote"]["USD"]["price"] - coin["fiyat"]
                toplam_maliyet = coin["miktar"] * coin["fiyat"]
                toplam_karzarar = coin_basina_karzarar * coin["miktar"]
                portfoy_karzarar = portfoy_karzarar + toplam_karzarar

                name = Label(window, text=coin["sembol"], bg=rgb_color((0, 0, 128)), fg='white',
                             borderwidth=3, relief='raised', padx=2, pady=2)
                name.grid(row=satir_no, column=0, sticky=N + S + W + E)

                price = Label(window, text="${0:.2f}".format(coin["fiyat"]), fg=rgb_color((0, 0, 128)), bg='white',
                              borderwidth=3, relief='sunken', padx=2, pady=2)
                price.grid(row=satir_no, column=1, sticky=N + S + W + E)

                no_coins = Label(window, text=coin["miktar"], bg=rgb_color((0, 0, 128)), fg='white',
                                 borderwidth=3, relief='groove', padx=2, pady=2)
                no_coins.grid(row=satir_no, column=2, sticky=N + S + W + E)

                amount_paid = Label(window, text="${0:.2f}".format(toplam_maliyet), fg=rgb_color((0, 0, 128)),
                                    bg='white', borderwidth=3, relief='ridge', padx=2, pady=2)
                amount_paid.grid(row=satir_no, column=3, sticky=N + S + W + E)

                all_amount_paid = all_amount_paid + toplam_maliyet

                current_val = Label(window, text="${0:.2f}".format(result["data"][i]["quote"]["USD"]["price"]),
                                    bg=rgb_color((0, 0, 128)), fg='white',
                                    borderwidth=3, relief='flat', padx=2, pady=2)
                current_val.grid(row=satir_no, column=4, sticky=N + S + W + E)

                pl_coin = Label(window, text="${0:.2f}".format(coin_basina_karzarar), fg=rgb_color((0, 0, 128)),
                                bg='white', borderwidth=3, relief='groove', padx=2, pady=2)
                pl_coin.grid(row=satir_no, column=5, sticky=N + S + W + E)
                # "${0:.2f}".format(toplam_karzarar)
                total_pl = Label(window, text=tl_formatla(toplam_karzarar), bg=rgb_color((0, 0, 128)),
                                 fg=font_color_pl(toplam_karzarar), borderwidth=3, relief='groove',
                                 padx=2, pady=2, anchor='e')
                total_pl.grid(row=satir_no, column=6, sticky=E + W)

                satir_no = satir_no + 1

    all_amount_paid = Label(window, text="${0:.2f}".format(all_amount_paid), fg=rgb_color((0, 0, 128)), bg='white')
    all_amount_paid.grid(row=satir_no, column=3, sticky=N + S + W + E)

    portfolio_pl = Label(window, text="${0:.2f}".format(portfoy_karzarar), bg=rgb_color((0, 0, 128)), fg='white')
    portfolio_pl.grid(row=satir_no, column=6, sticky=N + S + W + E)

    update_button = Button(window, text='Update',
                           bg='blue', fg='white', font='Lato 12',
                           command=my_portfolio)
    update_button.grid(row=satir_no + 1, column=6, sticky=W + E)
    # print('**************************')
    # print("Portföy Kar/Zarar: ${0:.2f}".format(portfoy_karzarar))
    # print('**************************')


window = Tk()
window.title('My Coin Portfolio')
window.iconbitmap('favicon.ico')
window.geometry('585x130')
center_window(585, 130)

name = Label(window, text='Coin Name', bg=rgb_color((0, 0, 128)), fg='white',
             borderwidth=3, relief='raised', padx=2, pady=2)
name.grid(row=0, column=0, sticky=N + S + W + E)

price = Label(window, text='Price', fg=rgb_color((0, 0, 128)), bg='white',
              borderwidth=3, relief='sunken', padx=2, pady=2)
price.grid(row=0, column=1, sticky=N + S + W + E)

no_coins = Label(window, text='Coin Owned', bg=rgb_color((0, 0, 128)), fg='white',
                 borderwidth=3, relief='groove', padx=2, pady=2)
no_coins.grid(row=0, column=2, sticky=N + S + W + E)

amount_paid = Label(window, text='Total Amount Paid', fg=rgb_color((0, 0, 128)), bg='white',
                    borderwidth=3, relief='ridge', padx=2, pady=2)
amount_paid.grid(row=0, column=3, sticky=N + S + W + E)

current_val = Label(window, text='Current Value', bg=rgb_color((0, 0, 128)), fg='white',
                    borderwidth=3, relief='flat', padx=2, pady=2)
current_val.grid(row=0, column=4, sticky=N + S + W + E)

pl_coin = Label(window, text='P/L Per Coin', fg=rgb_color((0, 0, 128)), bg='white',
                borderwidth=3, relief='groove', padx=2, pady=2)
pl_coin.grid(row=0, column=5, sticky=N + S + W + E)

total_pl = Label(window, text='Total P/L with Coin', bg=rgb_color((0, 0, 128)), fg='white',
                 borderwidth=3, relief='groove', padx=2, pady=2)
total_pl.grid(row=0, column=6, sticky=N + S + W + E)

my_portfolio()

window.mainloop()

cursor.close()
con.close()
