# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# def digits(num):
#     return sum(map(int, num.replace('.','')))
# num = input('Введите число: ')
# print(f' Сумма цифр в числе = {digits(num)}')

num = input('Введите число: ')
summ = 0
for count in str(num):
    if count != '.':
        summ += int(count)
print('Сумма цифр в числе', 'равна',summ)