'''cat1 = int(input('Digite o valor do primeiro cateto: '))
cat2 = int(input('Digite o valor do segundo cateto: '))
hip = ((cat1 ** 2) + (cat2 ** 2))**(1/2)
print('O valor da hipotenusa é: {:.2f} '.format(hip))'''
from math import hypot
co = int(input('Digite o valor do primeiro cateto:'))
ca = int(input('Digite o valor do segundo cateto:'))
hip = hypot(co, ca)
print('O valor da hipotenusa é:', hip)
