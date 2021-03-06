from random import randint
cont = 0
print('----- Vamos jogar um par ou impar comigo ------')
while True:
    jogador = int(input('Digite um numero entre 0 e 10: '))
    opcao = str(input('Digite [P] p/ Par ou [I] p/ Impar: ')).strip().upper()[0]
    computador = randint(0, 10)
    result = jogador + computador
    par = result % 2
    if par == 0:
        if opcao == 'P':
            print(f'Parabéns! eu escolhi {computador} e você {jogador}, logo {result} é Par.')
            cont += 1
        else:
            print('Voce perdeu!')
            print(f'Eu escolhi o numero {computador}')
            break
    else:
       if opcao == 'I':
           print(f'Parabéns! eu escolhi {computador} e você {jogador}, logo {result} é Impar.')
           cont += 1
       else:
           print('Voce perdeu!')
           print(f'Eu escolhi o numero {computador}')
           break
print(f'Voce ganhou {cont} vezes')


