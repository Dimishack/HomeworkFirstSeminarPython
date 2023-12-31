"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""

print("Введите количество монеток: ")
quaMoney = int(input())
quaZero = 0
quaOne = 0
i = 1
print("Примечание: 0 - решкой, 1 - гербом")
while i <= quaMoney:
    print(f"Как будет лежать {i} монета:")
    side = int(input())
    if side == 0:
        quaZero += 1
        i += 1
    elif side == 1:
        quaOne += 1
        i += 1
    else:
        print("Данное значение не является \"0\" или \"1\"")
result = quaOne
if quaZero < quaOne:
    result = quaZero
print(f"Для того, чтобы монетки были повернуты одной стороной, нужно перевернуть {result} монеток")