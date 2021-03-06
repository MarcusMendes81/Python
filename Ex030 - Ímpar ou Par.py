n = int(input('Digite qualquer número: '))
resultado = n % 2   # resto da divisão por 2
if resultado == 0:
    print('O numero {} é par'.format(n))
else:
    print('O numero {} é impar'.format(n))

