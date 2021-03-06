dias = int(input('Infome a quantidade de dias: '))
km = float(input('Informe quantos km rodados:'))
total = (60 * dias) + (0.15 * km)
print('Você utilizou por {} e percorreu {}km, o total a pagar é {}R$'.format(dias, km, total))
