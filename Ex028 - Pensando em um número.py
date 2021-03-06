from random import randint
from time import sleep
print('Olá Jovem! Quero propor um desafio! ')
print('Tente adivinhar o número que estou pensando...')
computador = randint(0, 5) # o computador irá sortear um número int entre 0 e 5
print('-'*30)
jogador = int(input('Digite aqui um numero entre 0 e 5: ')) # jogador coloca insere o número
print('Processando...')
sleep(3) # função de espera, em segundos.

if computador == jogador:
    print('\nAcertô mizeravi! Pensamos no mesmo número!')
else:
    print('\nErrrrooouu! Eu pensei {} e tu digitou {}'.format(computador, jogador))


