import requests
from bs4 import BeautifulSoup
import re

linkDol = 'https://www.remessaonline.com.br/cotacao/cotacao-dolar'
htmlDol = requests.get(linkDol).content
soup = BeautifulSoup(htmlDol, 'html.parser')
dolar = soup.find('div', class_="style__Text-sc-15flwue-2 cSuXFv")
dolar = dolar.string
dolar = re.sub('[^0-9]', '', dolar)
dolar = float(dolar)/100
print(f'O preço do 1 dolar é de: R${dolar}')

linkBTC = 'https://www.binance.com/en/trade/BTC_BUSD?type=spot'
htmlBTC = requests.get(linkBTC).content
soup = BeautifulSoup(htmlBTC, 'html.parser')
precoBTCt = soup.find('title')
precoBTC = precoBTCt.string
precoBTC = re.sub('[^0-9]', '', precoBTC)
precoBTC = int(precoBTC)/100
precoBTCReal = precoBTC * dolar
print(f'O preço atual do Bitcoin em dolar é de: ${precoBTC}\n'
      f'O preço atual do Bitcoin em real é de: R${precoBTCReal:.2f}')

linkIBOV = 'https://br.advfn.com/bolsa-de-valores/bovespa/indice-bovespa-IBOV/cotacao'
htmlIBOV = requests.get(linkIBOV).content
soup = BeautifulSoup(htmlIBOV, 'html.parser')
ibovt = soup.find('span', class_="PriceTextUp")
ibov = ibovt.string
ibov = re.sub('[^0-9]', '', ibov)
ibov = float(ibov)/100
ibovDol = ibov/dolar
print(f'\nO preço atual do Ibovespa em real é: R${ibov}\n'
      f'O preço atual do Ibovespa em dolar é: ${ibovDol:.2f}')

