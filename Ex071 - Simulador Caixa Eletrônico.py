print('='*20, '\033[31mBEM VINDO AO M.V. BANK\033[0m', '='*20)  # imprimir na tela a propaganda
valor = int(input('Olá! Qual a quantia que você deseja retirar? ')) # Recebe o dado do usuário.
total = valor   # Define a variavel como parametro
ced = 50    # A variavel recebe o valor maximo da nota para que possa subtrair as cedulas
totced = 0  # Essa variavel tem o intuito de contar as cedulas que serão imprimidas na tela
while True:
    if total >= ced: # Verifica se o valor digitado pelo usuário é maior que 50
        total -= ced # Decrementa do valor inserido pelo usuário, no caso o decremento é de 50 R$
        totced += 1  # Variavel com a função de contar a quantidade de cedulas que foram decrementadas do valor total
    else:
        if totced > 0: # Condição para eliminar a quantidade [0] de cedulas  na tela
            print(f'O total de {totced} cedulas de {ced} R$') # Imprime as quantidades e as cédulas na tela
        if ced == 50: # Função com intuito de trocar o valor da cedula e com isso poder imprimir
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0: # Depois que for subtraído tudo o programa encerra!
            break
