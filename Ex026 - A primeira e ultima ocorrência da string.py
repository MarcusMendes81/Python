frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} nesta frase'.format(frase.count('A')))
print('Em que posição ela aparece a primeira vez: ', frase.find('A')+1)
print('Em que posição ela aparece pela ultima vez: ', frase.rfind('A')+1) # o rfind lê da direita p/ esquerda


