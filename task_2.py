"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
   Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

def get_num_order(a):
    res = '';
    for i in range(a):
      res += '0'
    return int('1' + res)


#print(' test -> ' + str( get_num_order(5) ) )

a = int(input('Введите натуральное число:'))
leng = len(str(a))

print('Число ' + str(a) + ', длина числа ' + str(leng))
even_num = 0
not_even_num = 0

# Анатомичка
for i in range(leng, 0, -1):
    order = get_num_order(i-1)
    #print('Порядок = ' + str(order))
    aa , bb = divmod(a, order)
    #print( str(aa) + ', ' + str(bb))
    if aa % 2:
        not_even_num += 1
    else:
        even_num += 1

    a = a - aa * order
    print('a = ' + str(a))

print(' Количество четных цифр: ' + str(even_num))
print(' Количество не четных цифр: ' + str(not_even_num))




