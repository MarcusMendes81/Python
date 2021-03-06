extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um valor entre 0 e 20: '))
    if num >= 0 and num <=20:
        resposta = str(input('Você deseja continuar? [ S / N ]: ')).upper().strip()
        if resposta == 'S':
            num = int(input('Digite um valor entre 0 e 20: '))
        else:
            if resposta == 'N':
                break
    print('Numero inválido, digite novamente: ')
print(f'Voce digitou o numero {extenso[num]}')

