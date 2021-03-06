velocidade = float(input('Digite a sua velocidade em km: '))
multa = (velocidade - 80) * 7.0
if velocidade > 80:
    print('Você excedeu o limite de velocidade! \nO valor total da sua multa é {}R$'.format(multa))
else:
    print('Muito bem! Continue dirigindo com segurança!')