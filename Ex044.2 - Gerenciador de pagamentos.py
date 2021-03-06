print('{:=^40}'.format('BEM VINDO AS LOJAS MENDES'))
produto = float(input('Informe o valor do produto: R$ '))
opcao = int(input('''Escolha uma das opções de pagamento:
[ 1 ] À VISTA               10% de desconto
[ 2 ] À VISTA NO CARTÃO     5% de desconto
[ 3 ] EM ATÉ 3x NO CARTÃO   preço formal
[ 4 ] EM 4x OU MAIS         20% de juros
 '''))

if opcao == 1:
    total = produto - (produto * 10/100)
elif opcao == 2:
    total = produto - (produto * 5/100)
elif opcao == 3:
    parcela = int(input('Quantas parcelas? '))
    totalparc = produto / parcela
    total = produto
    if parcela <= 3:
       print('Sua compra sera divida em {:.2f} de {:.2f}'.format(parcela, totalparc))
    else:
        print('Opção inválida')
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    if parcela > 3 :
        total = (produto + (produto * 20 / 100))
        totalparc = (produto + (produto * 20 /100)) / parcela
        print('Sua compra será dividida em {:.2f}R$ de {:.2f}R$'.format(parcela, totalparc))
else:
    total = produto
    print('Opção inválida')
print('Sua compra de {:.2f}R$ terá um total de {:.2f}R$'.format(produto, total))


