"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

print("Введите маскимальное число: ")
max = int(input())
i = 1
print("Список целых чисел в степени 2:")
while i <= max:
    print(i)
    i*=2