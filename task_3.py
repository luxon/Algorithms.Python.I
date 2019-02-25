"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
   Например, если введено число 3486, то надо вывести число 6843.
"""

def get_num_order(a):
    res = '';
    for i in range(a):
      res += '0'
    return int('1' + res)

a = int(input('Введите целое число:'))
leng = len(str(a))

res = ''

# Анатомичка
for i in range(0, leng):
    order = get_num_order(i+1)
    #print('order = ' + str(order))
    aa , bb = divmod(a, order)
    bb = int(bb/get_num_order(i))
    #print('aa = ' + str(aa) + ', bb = ' + str(bb))
    res += str( bb )
    a = a - bb * get_num_order(i)
    #print('a = ' + str(a))

print('Обратное число ' + res)
