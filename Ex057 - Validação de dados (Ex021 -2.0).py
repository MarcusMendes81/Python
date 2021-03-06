sexo = str(input('Informe o sexo [M / F]: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Sexo inválido, informe novamente seu sexo [M / F]:  ')).upper().strip()
print('Sexo {} registrado com sucesso ! '.format(sexo))
