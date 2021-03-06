from random import randint

valor = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados são: {valor}')
ordem = sorted(valor)
print(f'\nO maior valor sorteado é {ordem[4]} e o menor é {ordem[0]}')

