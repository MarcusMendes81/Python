from time import sleep
import random

print('''\033[1:36mVAMOS JOGAR JOKENPO?
\033[0:mEscolha: Pedra, Papel ou Tesoura''')
jogador = str(input('\033[1:31mEscolha ---> ')).strip().upper()
lista = str('pedra papel tesoura').upper().lower().split()
computador = random.choice(lista)
encontrar = ('PEDRA' in jogador) or ('PAPEL' in jogador) or ('TESOURA' in jogador)

if encontrar:
    print('\033[1:37mJOOOOO')
    sleep(1)
    print('KEEEN')
    sleep(1)
    print('PO!')
    sleep(1)
    if jogador == computador:
        print('\033[1:35mEmpate! Nós escolhemos {}'.format(computador))
    elif (jogador == str('PEDRA') and computador == str('TESOURA')) or (
            jogador == str('TESOURA') and computador == str('PAPEL')) or (
            jogador == str('PAPEL') and computador == str('PEDRA')):
        print('\033[1:33mVocê ganhou! eu escolhi \033[1:30m{}\033[1:33mDroga!'.format(computador))
    elif (computador == str('PEDRA') and jogador == str('TESOURA')) or (
            computador == str('TESOURA') and jogador == str('PAPEL')) or (
            computador == str('PAPEL') and jogador == str('PEDRA')):
        print('Você perdeu! eu escolhi {}'.format(computador))
else:
    print('Nome inválido')
