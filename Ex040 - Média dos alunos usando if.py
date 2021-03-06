n1 = float(input('Digite a primeira nota do(a) aluno(a): '))
n2 = float(input('Digite a segunda nota do(a) aluno(a):  '))
media = (n1 + n2)/2

if media >= 7:
    print('Aluno \033[1:36mAPROVADO!\033[0:m sua média é: {:.2f}'.format(media))
elif media <= 4:
    print('Aluno \033[1:31mREPROVADO!!\033[0:m Sua média é: {:.2f}'.format(media))
else:
    print('Aluno em \033[1:32mRECUPERAÇÃO!!\033[0:m Sua média é: {:.2f}'.format(media))
