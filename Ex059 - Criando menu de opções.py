from time import sleep
opcao = [1, 2, 3, 4, 5]
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor:  '))
while opcao != 5:
    sleep(1)
    print(''' Escolha uma das opções
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior numero
    [ 4 ] Inserir novos números
    [ 5 ] Encerrar o programa
    ''')
    print('-='*15)
    opcao = int(input('Qual a opção? '))
    if opcao == 1:
         print('A soma entre {} e {} é de {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A subtração entre {} e {} é de {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior numero entre {} e {} é o {}'.format(n1, n2, n1))
        else:
            print('O maior numero entre {} e {} é o {}'.format(n1, n2, n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor:  '))
    elif opcao == 5:
        print('Encerrando . . .')
        sleep(2)
        print('Seu programa foi encerrado com sucesso !')
    else:
        print('Opção inválida !     Tente de novo !')
        sleep(1)
        print('-='*15)

