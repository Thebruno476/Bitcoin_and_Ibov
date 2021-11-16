import requests

class Dolar_Value:
    def __init__(self):
        self.url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
        self.req = requests.get(self.url).json()

    def get_price(self):
        self.price = self.req['USDBRL']['bid']
        return f'R$ {float(self.price):.2f}'

    def calculate_value(self, dolars):
        self.price = self.get_price()
        self.price = self.price[2:]
        self.dolars_value = float(self.price) * float(dolars)
        return f'R$ {dolars:.2f}'