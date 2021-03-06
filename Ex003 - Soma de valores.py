num1 = int(input('\033[1:30mDigite um valor: '))
num2 = int(input('\033[1:30mDigite outro valor: '))
result = num1 + num2

print('\033[1:30mA soma dos valores \033[1:33m{} e \033[1:31m{} \033[1:30mé igual a \033[1:36m{} \033[1:30m\nObrigado!'.format(num1,num2,result))