print('='*10, 'Gerando uma PA', '='*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o valor da razão: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(' {} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você deseja? '))
print('Fim')
print('Progressão aritimética finalizada com {} termos'. format(total))
