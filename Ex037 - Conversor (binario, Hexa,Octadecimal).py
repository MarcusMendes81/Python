num = int(input('Digite qualquer número: '))
print('''Escolha uma dessas opções abaixo para conversão
[ 1 ] para BINÁRIO 
[ 2 ] para OCTADÉCIMAL
[ 3 ] para HEXADÉCIMAL''')
num1 = int(input('Faça sua escolha: '))

binario = str(bin(num)[2:])
ocatadecimal= str(oct(num)[2:])
hexadecimal = str(hex(num)[2:])
if num1 == 1:
    print('O número em binário é: ', end='')
    print(binario)
elif num1 == 2:
    print('O número em Octadecimal é: ', end='')
    print(ocatadecimal)
elif num1 == 3:
    print('O numero em Hexadecimal é:', end='')
    print(hexadecimal)
else:
    print('Opção inválida!')


