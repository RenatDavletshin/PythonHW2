# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

num = int(input('Введите число:'))
my_list = []
for i in range(num):
    my_list.append(random.randint(-num, num))
print(my_list)