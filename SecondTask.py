"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""

print("Введите первую подсказку (сумма 2 Ваших чисел): ")
sum = int(input())
print("Введите вторую подсказку (произведение 2 Ваших чисел): ")
mult = int(input())
first = 1
while first < sum:
    second = sum - first
    if first * second == mult:
        print("Числа отгаданы. Первое число: {}, второе: {}".format(first, second))
        exit()
    first += 1
print("Числа не отгаданы.")