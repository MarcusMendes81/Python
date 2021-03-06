from random import randint

valor = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for c in valor:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado é {max(valor)}')
print(f'O menor valor sorteado é {min(valor)}')
