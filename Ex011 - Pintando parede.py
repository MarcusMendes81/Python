altura = float(input('Digite a altura em metros:'))
largura = float(input('Digite o largura em metros:'))
area = altura*largura
tinta = area/2

print('A dimensão é {}x{} e sua área é {:.2f}m²'.format(altura, largura, area))
print('A quantidade de tinta necessária é de {:.2f} Litros'.format(tinta))
