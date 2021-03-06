preco = float(input('Digite o valor do produto: R$'))
vista = preco-(preco*10/100)
parc = preco+(preco*8/100)

print('O valor do produto é: {}R$ \nPagamento à vista terá um desconto de 10%, total de {}R$ \nA prazo terá um acréscimo de 8%, total de {:.2f}R$'.format(preco,vista,parc))