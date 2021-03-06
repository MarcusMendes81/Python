num = int(input('Digite um numero: '))
'''total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(' {} '.format(c), end='')
print('\033[0m\nEle é divisível por {} vezes'.format(total))
if total == 2:
    print('\033[32mEste numero é primo')
else:
    print('\033[31mEste numero não é primo')'''

if num == 2 or num == 3 or num == 5:
    print('Este numero é primo')
elif num % 2 == 0 or num % 3 == 0:
    print('este numero não é primo')
else:
    print('É primo')