from datetime import date
nome = str(input('Informe o primeiro e ultimo nome do(a) atleta: ')).strip().title()
nasc = int(input('Informe o ano de nascimento do(a) atleta: '))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('{} tem {} anos e está na categoria: \033[1:31mMIRIM '.format(nome, idade))
elif idade <= 14:
    print('{} tem {} anos e está na catergoria: \033[1:32mINFANTIL'.format(nome, idade))
elif idade <= 19:
    print('{} tem {} anos e está na categoria: \033[1:33mJUVENIL'.format(nome, idade))
elif idade <= 25:
    print('{} tem {} anos e está na categoria: \033[1:34mSÊNIOR'.format(nome, idade))
else:
    print('{} tem {} anos e está na categoria: \033[1:34mMASTER'.format(nome, idade))
