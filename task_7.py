"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
   1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""

def get_row(n):
    i = 1
    sum = 0
    while True:
        sum += i
        if i == n:
            break
        i += 1
    return sum

def get_formula(n):
    return n*(n + 1)/2;

#print(str(get_row(5)))

a = int(input('Введите натуральное число:'))

if get_row(a) == get_formula(a):
    print('Верно: 1+2+...+n = n(n+1)/2')
else:
    print('Не Верно: 1+2+...+n = n(n+1)/2')
