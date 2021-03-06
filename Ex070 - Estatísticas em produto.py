print('='*20, 'Lojão dos eletrônicos! ', '='*20)
prod_atual = menor = total = cont = tot1000 = 0
while True:
    prod = str(input('Qual o produto você está comprando? ')).strip().upper()
    preco = int(input('Qual o preço deste produto?R$  '))
    novo = ' '
    while novo not in 'SN':
        novo = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    cont += 1
    total += preco
    if cont == 1 or preco < menor:
        menor = preco
        prod_atual = prod
    if preco > 1000:
        tot1000 += 1
    if novo == 'N':
        break
print('-'*20, 'FIM DO PROGRAMA', '-'*20)
print(f'Voce comprou {cont} itens com o valor total de {total:.2f}R$')
print(f'Você comprou {tot1000} produto(s) acima de 1000 R$')
print(f'O produto mais barato foi {prod_atual} que custou {menor:.2f}R$')