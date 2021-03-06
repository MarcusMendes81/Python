km = float(input('Digite qual a distância da sua viagem em km: '))

if km <= 200:
    preço = km * 0.50
    print('O valor da sua viagem é de {:.2f}R$'.format(preço))
else:
    preço = km * 0.45
    print('O valor da sua viagem é de {:.2f}R$'.format(preço))
