from random import randint
print('------ Jogo da Adivinhação ------ ')
jogador = int(input('Escolha um número entre 0 e 5 e tente adivinhar em qual numero eu pensei: '))
computador = randint(1, 10)
contador = 1
while computador != jogador:
    if computador > jogador:
       jogador = int(input('\033[31mMais... Tente de novo: '))
    else:
        jogador = int(input('\033[32mMenos... Tente de novo: '))
    contador += 1
print('\033[35mParabéns você adivinhou!')
print('Voce acertou na {}ª tentativa'.format(contador))
