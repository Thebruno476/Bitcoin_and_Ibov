from bot.bitcoin import Bitcoin
from bot.dolar import Dolar_Value
from bot.ibovespa import Ibov

use_program = int(input('Deseja usar o programa:\n1) Sim\n2) Não\n'))
while use_program not in [1, 2]:
    print('Opção invalida')
    use_program = int(input('Deseja usar o programa:\n1) Sim\n2) Não\n'))
while use_program == 1:
    user_option = int(input('1) Ver o preço do Bitcoin\n2) Ver o valor de uma carteira de Bitcoins\n'
                            '3) Ver o preço do dolar\n4) Ver o valor para uma quantidade x de Dolares\n'
                            '5) Preço do Bitcoin em dolar \n'
                            '6) Preço de uma carteira com x Bitcoins em dolares\n'
                            '7) Ver o preço do Ibovespa \n8) Ver o preço do Ibovespa em dolar\n'
                            '9) Ver o preço do Ibovespa em Bitcoin\n'))
    while user_option not in range(1, 10):
        print('Opção invalida')
        user_option = int(input('1) Ver o preço do Bitcoin\n2) Ver o valor de uma carteira de Bitcoins\n'
                            '3) Ver o preço do dolar\n4) Ver o valor para uma quantidade x de Dolares\n'
                            '5) Preço do Bitcoin em dolar \n'
                            '6) Preço de uma carteira com x Bitcoins em dolares\n'
                            '7) Ver o preço do Ibovespa \n8) Ver o preço do Ibovespa em dolar\n'
                            '9) Ver o preço do Ibovespa em Bitcoin\n'))
    if user_option == 1:
        print(f'R$ {Bitcoin().get_price():.2f}')
    elif user_option == 2:
        user_bitcoins = float(input('Digite a quantidade de Bitcoin que deseja ver o preço em reais: '))
        print(Bitcoin().calculate_value(user_bitcoins))
    elif user_option == 3:
        print(Dolar_Value().get_price())
    elif user_option == 4:
        user_dolars = float(input('Digite a quantidade de Dolares que deseja calcular: '))
        print(Dolar_Value().calculate_value(user_dolars))
    elif user_option == 5:
        bitcoin = Bitcoin().get_price()
        dolar = Dolar_Value().get_price()
        print(f'$ {float(bitcoin[3:]) / float(dolar[3:]):.2f}')
    elif user_option == 6:
        user_bitcoins = float(input('Digite a quantidade de Bitcoin que deseja vere o preço em dolar: '))
        bitcoin = Bitcoin().calculate_value(user_bitcoins)
        dolar = Dolar_Value().get_price()
        price = float(bitcoin[3:]) / float(dolar[3:])
        print(f'${price:.2f}')
    elif user_option == 7:
        print(f'{Ibov().get_price()}')
    elif user_option == 8:
        ibov = Ibov().get_price()
        dolar = Dolar_Value().get_price()
        print(f'$ {(float(ibov[3:]) / float(dolar[3:])):.2f}')
    elif user_option == 9:
        ibov = Ibov().get_price()
        bitcoin = Bitcoin().get_price()
        print(f'₿ {(float(ibov[3:]) / float(bitcoin[3:])):.2f}')
    use_program = int(input('Deseja usar o programa novamente:\n1) Sim\n2) Não\n'))
    while use_program not in [1, 2]:
        print('Opção invalida')
        use_program = int(input('Deseja usar o programa:\n1) Sim\n2) Não\n'))