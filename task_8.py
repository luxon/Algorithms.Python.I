"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
   и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""

def get_num_order(a):
    res = '';
    for i in range(a):
      res += '0'
    return int('1' + res)

a = int(input('Введите количество чисел которые ты хочешь посчитать:'))
b = int(input('Введите число которое ты хочешь посчитать:'))

ch = 0
sum = 0
for i in range(0, a):
    ch = int(input('Введите число ' + str(i+1) + ':'))
    leng = len(str(ch))

    # Анатомичка
    for ii in range(0, leng):
        order = get_num_order(ii + 1)
        #print('order = ' + str(order))
        aa, bb = divmod(ch, order)
        bb = int(bb / get_num_order(ii))
        #print('aa = ' + str(aa) + ', bb = ' + str(bb))
        if b == bb:
            sum += 1
        ch = ch - bb * get_num_order(ii)
        #print('ch = ' + str(ch))

print('В введенных тобой числах число ' + str(b) + ' встречается ' + str(sum) + ' раз(а)')
