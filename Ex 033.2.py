n1 = int(input('Digite um primeiro número qualquer: '))
n2 = int(input('Digite um segundo número qualquer: '))
n3 = int(input('Digite um terceiro número qualquer: '))
menor = n1
maior = n1
if n2 < n1:
    menor = n2
if n3 < n1:
    menor = n3
if n2 > n1:
    maior = n2
if n3 > n1:
    maior = n3

print('O menor numero digitado foi: ', menor)
print('O maior numero digitado foi: ', maior)