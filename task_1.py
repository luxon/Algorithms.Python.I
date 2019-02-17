"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

a = int(input('Введите 3х значное число от 0 до 999:'))
ch_100=0
ch_10=0
ch_1=0

main_b, _ = divmod(a,100)
ch_100 = main_b
main_c, ostatok_c = divmod(a-100*main_b, 10)
ch_10 = main_c
ch_1 = ostatok_c
"""
print(ch_100)
print(ch_10)
print(ch_1)
"""
print('Результат суммы = ' + str(ch_1 + ch_10 + ch_100))
print('Результат произведения = ' + str(ch_1*ch_10*ch_100))

