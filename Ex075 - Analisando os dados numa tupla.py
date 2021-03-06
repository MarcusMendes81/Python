print('Digite 4 números !')
numeros = (int(input('Digite o 1° numero: ')), int(input('Digite o 2° numero: ')),
           int(input('Digite o 3° numero: ')), int(input('Digite o 4° numero: ')))
print(f'Os valores digitados foram respectivamente: {numeros}')
print(f'O numero 9 foi digitado {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 foi digitado na {numeros.index(3)+1}ª posição')
else:
    print('O numero 3 não foi digitado ! ')
print('Os numeros pares digitados foram', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')