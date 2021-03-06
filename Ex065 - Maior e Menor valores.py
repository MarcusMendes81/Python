menor = maior = cont = soma = n = 0
continuar = 's' or 'n'
while continuar == 's':
    n = int(input('Digite um valor: '))
    continuar = str(input('Você deseja continuar [S / N]? ')).strip().lower()
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
          menor = n
print('Você digitou {} números e a soma total foi de {}'.format(cont, soma))
print('A media entre os números é de {:.2f} o maior valor digitado foi {} e o menor foi {} '.format(media, maior, menor))

