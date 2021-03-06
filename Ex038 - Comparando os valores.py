num1 = int(input('Digite um valor inteiro: '))
num2 = int(input('Digite outro valor inteiro: '))

if num1 > num2:
    print('O \033[1:33mPRIMEIRO\033[0:m valor é maior')
elif num1 < num2:
    print('O \033[1:33mSEGUNDO\033[0:m valor é maior')
else:
    print('Não há maior, \033[1:33mAMBOS\033[0:m são iguais')