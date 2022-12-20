# Напишите программу, принимает на вход число N и выдает набор из произведений от 1 до N.

# N = int(input('Введите число:'))
# x = 1
# for y in range(N):
#     y = y + 1
#     x = y * x
# print(x)

N = int(input('Введите число: '))
num = []
value = 1
for i in range(1, N + 1):
    num.append(value)
    value *= i + 1
print(num)