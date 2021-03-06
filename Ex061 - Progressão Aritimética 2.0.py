print('='*10, 'Gerando uma PA', '='*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o valor da razão: '))
cont = 1
termo = primeiro
while cont <= 10:
    print(' {} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')
