print('-=' * 5, ' SEQUENCIA FIBONACCI ', '-=' * 5)
termo = int(input('Quantos termos você deseja? '))
cont = 3
primeiro = 0
segundo = 1
print('{} -> {} -> '.format(primeiro, segundo), end='')
while cont <= termo:
    soma = primeiro + segundo
    print(' {} ->'.format(soma), end='')
    cont += 1
    primeiro = segundo
    segundo = soma
    soma = primeiro + segundo
print(' Fim ')