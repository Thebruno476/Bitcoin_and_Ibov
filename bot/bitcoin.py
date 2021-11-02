import requests

class Bitcoin:
    def __init__(self):
        self.url = 'https://www.mercadobitcoin.net/api/btc/ticker'
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
        self.req = requests.get(self.url, headers=self.headers).json()

    def get_price(self):
        self.price = self.req['ticker']['last']
        return f'R$ {float(self.price):.2f}'

    def calculate_value(self, my_sats):
        self.price = self.get_price()
        self.my_sats = my_sats
        self.my_wallet = float(self.price[3:]) * float(self.my_sats)
        return f'R$ {self.my_wallet:.2f}'
