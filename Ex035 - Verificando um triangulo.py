
r1 = float(input('Digite o primeiro segmento de reta: '))
r2 = float(input('Digite o segundo segmento de reta:  '))
r3 = float(input('Digite o terceiro segmento de reta: '))

if abs(r1-r2) < r3 < r1 + r2:
    print('Esses segmentos podem formar um triângulo')
else:
    print('Esses segmentos NÃO podem formar um triângulo')
