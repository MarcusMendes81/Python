print('='*20, 'CADASTRO DE IDADE E SEXO ', '='*20)
maior = mulher = homem = 0
while True:
    idade = int(input('Digite uma idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [ M / F ]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'F' and idade < 20:
            mulher += 1
    if sexo == 'M':
        homem += 1
    novo_cad = ' '
    while novo_cad not in 'SN':
        novo_cad = str(input('Você deseja cadastrar outra pessoa? [S/N] ')).strip().upper()[0]
        print('=' * 30)
    if novo_cad == 'N':
        break
print('CADASTRO FINALIZADO COM SUCESSO!!!')
print(f'''O Total de pessoas cadastradas acima de 18 anos: {maior}
O Total de homens cadastrados                    {homem}
O Total de mulheres abaixo de 20 anos:           {mulher} ''')
