# Задача 1:
# Вычислить число Пи c заданной точностью d

# import math 
# a = math.pi

# d = input().split(sep='.')
# num = len(d[1])

# print(round(a, num))

# Задача 2:
# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# a = int(input('Введите число '))
# b = a
# i = 2
# numbers = []

# while i <= b:
#     if b % i == 0:
#         numbers.append(i)
#         b //= i
#         i = 2
#     else:
#         i += 1
# print(f'Простые множители числа {a}: {numbers}')

# Задача 3: 
#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

N = [2, 2, 2, 3, 3, 4, 5, 5, 5, 5]
unique = []

for i in N:
    if i not in unique:
        unique.append(i)

print(*unique)