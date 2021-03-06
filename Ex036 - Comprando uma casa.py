from time import sleep

casa = int(input('\033[1:30mDigite o valor total do imóvel: '))
salario = float(input('\033[1:30mQual o valor bruto do seu salário: '))
prazo = int(input('\033[1:30mEm quantos anos deseja quitar o imóvel: '))

parcela = casa / (12 * prazo)
minimo = (salario * 30/100)
sleep(1)
print('\033[1:32mSó será permitido dividir em até 50 anos')
sleep(2)
print('\033[1:30mVerificando . . .')
sleep(3)

if parcela <= minimo:
    print('\033[1:34mSeu empréstimo será concedido!')
    print('Para pagar o valor total do imóvel {}RS em {} anos a prestação mensal será de {:.2f}R$'.format(casa, prazo, parcela))
else:
    print('\033[1:31mInfelizmente o seu empréstimo não poderá ser concedido!')
    print('Para pagar o valor total do imóvel {}RS em {} anos a prestação mensal será de {:.2f}R$ e você só tem  {}R$'.format(casa, prazo, parcela, minimo))



