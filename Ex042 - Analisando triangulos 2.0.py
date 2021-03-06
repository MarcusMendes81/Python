from time import sleep
lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo:  '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))

triangulo = (lado1 - lado2 < lado3 < lado1+lado2)

if triangulo == True:
    print('Essas retas formam um triangulo')
    sleep(1)
    if lado1 == lado2 == lado3:
        print('Essas retas formam um triângulo \033[1:32mEQUILÁTERO.')
    elif lado1 != lado2 != lado3 != lado1:
        print('Essas retas formam um triângulo \033[1:33mESCALENO')
    else:
        print('Essas retas formam um triângulo \033[1:31mISÓSCELES')
else:
    print('Essas retas não formam um triângulo')
