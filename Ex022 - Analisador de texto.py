nome = str(input('Digite seu nome completo: '))
print('O seu nome em maísculo: ',nome.upper())
print('O seu nome em minúsculas: ', nome.lower())

# ==== algoritmo para contar a quantidade de letras sem os espaços ======
divisao = nome.split()       # divide a string em forma de lista;
uniao = ''.join(divisao)   # "Salva" a divisão anterior na mesma variável e depois
                             # une as strings dentro da lista, assim eliminando os espaços;

print('Seu nome completo tem {} letras'.format(len(uniao)))          # Conta o tamanho todos os caratceres.
print('E seu primeiro nome tem {} letras'.format(len(divisao[0])))


