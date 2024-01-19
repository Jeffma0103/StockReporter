import twstock
import requests
class GetData:
    def __init__(self, stockid):
        self.stockid = stockid

    def get_price(self):
        price = twstock.realtime.get(self.stockid)
        if price['success']:
            return (price['info']['name'], float(price['realtime']['latest_trade_price']))
        else:
            return (False, False)




test = GetData("2330")

test.get_price()