print('-'*10, 'Tabuada 3.0', '-'*10)
while True:
    num = int(input('Digite qual o valor da tabuada que voce deseja: '))
    print('-' * 25)
    if num < 0:
        break
    for cont in range(1, 11):
        mult = num * cont
        print(f'{cont} x {num} = {mult}')
print('Programa de Tabuada encerrada com sucesso!')

