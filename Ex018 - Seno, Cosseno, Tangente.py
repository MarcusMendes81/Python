import math
num = int(input('Digite o ângulo que você deseja: '))
'''convert = math.radians(num)
print('O ângulo de {} tem o SENO de {:.2f}'.format(num, math.sin(convert)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(num, math.cos(convert)))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(num, math.tan(convert)))'''

Cosseno = math.cos(math.radians(num))
Seno = math.sin(math.radians(num))
Tangente = math.tan(math.radians(num))

print('O SENO de {} é {:.2f}\nO COSSENO de {} é {:.2f} \nA TANGENTE de {} é {:.2f}'.format(num, Seno, num, Cosseno, num, Tangente))
