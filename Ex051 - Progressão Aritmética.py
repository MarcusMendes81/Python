n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
an = n + r*(10-1)
for i in range(n, an + r, r):
    print('{}'.format(i), end=' -> ')
print('ACABOU!')
