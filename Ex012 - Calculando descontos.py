preco = float(input('Insira o valor do produto: R$'))
porc = 20
desc = preco-(preco*porc/100)


print('O produto custava R${}, na promoção com desconto de {}% vai custar {}'.format(preco,porc,desc))