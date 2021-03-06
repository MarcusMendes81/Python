from time import sleep

nome = str(input('Digite seu nome completo: ')).strip().upper()
nome2 = nome.split()
print('''Olá \033[1:33m{} \033[1:33m{}\033[0:m prazer em lhe conhecer!
Iremos Analisar o seu  \033[1:31mIMC (Índice de Massa Corporal)\033[0:m'''.format(nome2[0], nome2[-1]))
sleep(2)

altura = float(input('Informe o valor da sua altura: '))
peso = float(input('Informe o valor do seu peso: '))
imc = peso / (altura ** 2)
pesoideal = str('o valor ideal do imc é entre 18.5 e 25')

print('Sua altura é de {}m e seu peso é {}kg'.format(altura, peso))
if imc <= 18.5:
    print('Seu imc é de {:.2f} Você está \033[1:36mMAGREZA\033[0:m'.format(imc))
    print(pesoideal)
elif 18.5 <= imc <= 25:
    print('Seu imc é de {:.2f} Você está \033[1:35mNORMAL\033[0:m'.format(imc))
elif 25 <= imc <= 30:
    print('Seu imc é de {:.2f} Você está \033[1:34mSOBREPESO\033[0:m'.format(imc))
    print(pesoideal)
elif 30 < imc <= 40:
    print('Seu imc é de {:.2f} Você está \033[1:33mOBESIDADE\033[0:m'.format(imc))
    print(pesoideal)
else:
    print('Seu imc é de {:.2f} Você está \033[1:32mOBESIDADE MORBIDA\033[0:m'.format(imc))
    print(pesoideal)



