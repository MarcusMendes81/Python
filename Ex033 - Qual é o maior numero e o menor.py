n1 = int(input('Digite um primeiro número qualquer: '))
n2 = int(input('Digite um segundo número qualquer: '))
n3 = int(input('Digite um terceiro número qualquer: '))


if n1 > n2 and n1 > n3:
    print('O maior valor digitado é: {}'.format(n1))
if n1 < n2 and n1 < n3:
    print('O menor valor é: {}'.format(n1))

if n2 > n1 and n2 > n3:
    print('O maior valor digitado é: {}'. format(n2))
if n2 < n1 and n2 < n3:
    print('O menor valor digitado é: {}'.format(n2))

if n3 > n1 and n3 > n2:
    print('O maior valor digitado é: {}'.format(n3))
if n3 < n1 and n3 < n2:
    print('O menor valor digitado é: {}'.format(n3))
