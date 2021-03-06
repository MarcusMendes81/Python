num = int(input('Digite um numero: '))
c = num
f = 1
print('O fatorial do numéro {} é:'.format(num))
for c in range(num, 0, -1):
    print(' {} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(' {} '.format(f))