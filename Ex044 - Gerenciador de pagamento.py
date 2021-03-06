produto = float(input('Infome o valor do produto (R$): '))
opcao = int(input('''Escolha uma forma de pagamento: 
[ 1 ] À VISTA  -------------------------10% de desconto
[ 2 ] À VISTA NO CARTÃO ---------------- 5% de desconto
[ 3 ] ATÉ 3x  NO CARTÃO S/JUROS -------- 0% de desconto
[ 4 ] ACIMA 3x NO CARTÃO C/ JUROS ----- 20%
  '''))

if opcao == 1:
    desc = produto - (produto * 10 / 100)
    print('Sua compra de {:.2f}R$ com desconto de 10% sairá {:.2f}R$'.format(produto, desc))
elif opcao == 2:
    desc = produto - (produto * 5 / 100)
    print('Sua compra de {:.2f} com desconto de 5% sairá {:.2f}R$'.format(produto, desc))
elif opcao == 3:
    qtdpar = int(input('Quantas parcelas? '))
    desc = produto
    parcela = produto / qtdpar
    if qtdpar <= 3:
        print('Sua compra de {:.2f}R$ será divida em {}x de {:.2f}R$'.format(desc, qtdpar, parcela))
        print('O valor final da sua compra será de {}R$'.format(produto))
    else:
        print('Opção Inválida')
elif opcao == 4:
     juros = produto + (produto * 20 / 100)
     qtdpar = int(input('Quantas parcelas? '))
     parcela = juros / qtdpar
     if qtdpar > 3 and qtdpar <= 10:
         print('Sua compra de {:.2f} será divida em {}x de {:.2f}R$'.format(produto, qtdpar, parcela))
         print('O valor final a pagar será de {:.2f}R$'.format(juros))
     else:
         print('Não dividimos mais do que isso!!!')
else:
    print('Opção inválida')