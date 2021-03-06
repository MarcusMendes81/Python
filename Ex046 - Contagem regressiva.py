from time import sleep
import emoji
print('\033[1:31mContagem regressiva para os fogos\033[0:m!!')
sleep(2)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[1:33mFeliz ano novo!!!\033[1:31m')
print(emoji.emojize(':fireworks:'*5))
