import requests
import json

def longstr_to_epoch(yyyy_mm_dd):
    yyyy = yyyy_mm_dd[:4] #get us the 1st 4 chars of the str
    yyyy_in_sec = (int(yyyy) - 1970) * (365.25 * 24 * 60 * 60) #get time as epoch

    mm = yyyy_mm_dd[5:7] #get us the month
    mm_in_sec = (int(mm) * 30 * 24 * 60 * 60)

    dd = yyyy_mm_dd[8:10] #get day
    dd_in_sec = (int(dd) * 24 * 60 * 60)

    return int(yyyy_in_sec + mm_in_sec + dd_in_sec)

def get_btc_price_info():
    coindesk_api = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=2019-09-18" #you can change end date and start date, looks like it screws up data with a too early start date

    r = requests.get(coindesk_api)
    j = json.loads(r.text)
    j=j["bpi"] #clear out all the other random garbage
    return j

price_info = get_btc_price_info()
prices = open("prices.txt", "w")
for date in price_info:
    prices.write(str(longstr_to_epoch(date)) + "," + str(price_info["{}".format(date)]) + "\n")

prices.close()
print("all required data has been saved to prices.txt, keep prices.txt in the same folder as the predictor")