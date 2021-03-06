cont_genero = 0
soma_idade = 0
media_idade = 0
maior_idade = 0
nome_atual = ''
for i in range(1, 5):
    print('-'*5, '{}ª pessoa'.format(i), '-'*5)
    nome = str(input('Insira o nome de uma pessoa: ')).strip().upper()
    idade = int(input('Insira a idade: '))
    genero = str(input('Qual o gênero? M / F\n')).strip().upper()
    soma_idade += idade
    media_idade = int(soma_idade / 4)
    if genero == 'F':
        if idade < 20:
            cont_genero += 1
    else:
        if i == 1 and genero == 'M':
            maior_idade = idade
            nome_atual = nome
        elif idade > maior_idade:
            maior_idade = idade
            nome_atual = nome
print('A media das idades é: {}'.format(media_idade))
print('A quantidade de mulheres abaixo dos 20 anos é de {}'.format(cont_genero))
print('O homem mais velho do grupo tem {} anos  e se chama é {}'.format(maior_idade, nome_atual), end=' ')

