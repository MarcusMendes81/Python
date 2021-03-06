contador = 0
acumulador = 0
for i in range(1, 7):
    n = int(input('Digite o {} valor: '.format(i)))
    if n % 2 == 0:
        contador += 1
        acumulador += n
print('Você informou o total de {} numeros, {} deles são pares e a soma desses pares é {}'.format(i, contador, acumulador))

