s = float(input('Qual é o salário do funcionário: R$'))
porc = 10
aumento = s+(s*porc/100)
print('Um funcionário ganhava {}R$, agora com um ameunto de {}% passará a receber {}R$'.format(s,porc,aumento))
