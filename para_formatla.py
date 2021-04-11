import locale


def standart_formatla(para):
    currency = "${:,.2f}".format(para)
    return currency


def tl_formatla(para):
    # dolar formatında yazmak istersek binlik =, ve ondalik=.
    # olmalı. Bunları parametrik de verebiliriz.
    binlik = "."
    ondalik = ","

    currency = "{:,.2f}".format(para)

    if binlik == ".":
        main, fractional = currency.split('.')[0], currency.split('.')[1]

        new_main = main.replace(',', '.')
        currency = '$' + new_main + ondalik + fractional + "TL"
    else:
        currency = '$' + currency
    return currency


def locale_turkish_formatla(para):
    locale.setlocale(locale.LC_ALL, "tr_TR.utf8")

    return locale.currency(para, grouping=True)


print(standart_formatla(12345678.91))
print(tl_formatla(12345678.91))
print(locale_turkish_formatla(12345678.91))

