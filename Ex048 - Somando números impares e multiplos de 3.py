cont = 0
total = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        total = total + c
print('todos os {} valores do intervalo de 1 a 500 tem uma soma de {}'.format(cont, total))

