from datetime import date
from time import sleep
ano = int(input('Digite um ano qualquer ou 0 para analisar o ano atual: '))
print('Analisando . . . ')
sleep(2)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} É um ano bissexto'.format(ano))
else:
    print('{} Não é um ano bissexto'.format(ano))
