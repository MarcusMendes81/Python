salario = float(input('Digite o salário do funcionário: '))
if salario > 1250.00:
    novo = (salario * 0.10) + salario
    print('O salário de {} terá um aumento de 10%, logo será de {}R$'.format(salario, novo))
else:
    novo = (salario * 0.15) + salario
    print('O salário de {} terá um aumento de 15%, logo será de {}R$'.format(salario, novo))
