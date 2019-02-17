"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

print('Введите, пожалуйста, 3 разных числа:')
ch_1 = int(input('Число 1:'))
ch_2 = int(input('Число 2:'))
ch_3 = int(input('Число 3:'))

if (ch_1 > ch_2 and ch_2 > ch_3) or (ch_3 > ch_2 and ch_2 > ch_1):
    print(' Это число ' + str(ch_2))
elif (ch_2 > ch_1 and ch_1 > ch_3) or (ch_3 > ch_1 and ch_1 > ch_2):
    print(' Это число ' + str(ch_1))
elif (ch_2 > ch_3 and ch_3 > ch_1) or (ch_1 > ch_3 and ch_3 > ch_2):
    print(' Это число ' + str(ch_3))
elif ch_1 == ch_2 or ch_2 == ch_3 or ch_1 == ch_3:
    print(' Нет среднего числа ')
else:
    print('Ошибка !')
