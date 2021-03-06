from datetime import date

nasc = int(input('Digite o seu \033[1:32mANO\033[0:m de nascimento: '))
atual = date.today().year

idade = atual - nasc
saldo = abs(idade - 18)
passado = nasc + 18

genero = int(input(''''Escola uma dessas opções:
 Digite [ 1 ] para Masculino 
 Digite [ 2 ] para Feminino
 '''))

if genero == 1:
    if atual - nasc == 18:
        print('Você tem {} e deve se apresentar ainda neste ano de {}!!'.format(idade, atual))

    elif atual - nasc > 18:
        print('''Você se alistou? Se não, você já passou do prazo!!
    Seu alistamento foi em {}, sua idade atual é {} anos'''.format(passado, idade))

    elif atual - nasc < 18:
        print('Voce ainda não completou idade para se alistar!')
        print('Faltam {} ano(s) para você se alistar!'.format(saldo))
        print('Você deve se alistar no ano de {}'.format(passado))
elif genero == 2:
    print('Você está dispensada da obrigatoriedade do alistamento militar')
else:
    print('\033[1:36mOpção inválida!')

