import requests
from bs4 import BeautifulSoup


class Ibov:
    def __init__(self):
        self.url = 'https://br.advfn.com/bolsa-de-valores/bovespa/indice-bovespa-IBOV/cotacao'
        self.req = requests.get(self.url).content
        self.soup = BeautifulSoup(self.req, 'html.parser')
        self.ibov_raw = self.soup.find('span', id="quoteElementPiece1").string
        self.ibov = self.ibov_raw.replace('.', '')
        self.ibov = self.ibov.replace(',', '.')

    def get_price(self):
        self.price = float(self.ibov)
        return f'R$ {self.price:.2f}'
