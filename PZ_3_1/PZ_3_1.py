# Вариант 12.
# 1. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Каждое из
# чисел A, B, C положительное».
print("Ваша задача ввести (!)ПОЛОЖИТЕЛЬНЫЕ(!) => (!)ЦЕЛЫЕ(!) числа")

a = input("Введите ваше первое число : ")
b = input("Введите ваше второе число : ")
c = input("Введите ваше третье число : ")

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("!", "Введите правильный тип данных", "!", sep=' ')
        a = input("Введите ваше число a: ")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("!", "Введите целоe положительное число", "!", sep=' ')
        b = input("Введите ваше число b: ")

while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("!", "Введите целоe положительное число", "!", sep=' ')
        c = input("Введите ваше число c: ")

if a > 0 and b > 0 and c > 0:
    print("True")
else:
    print("!", "False", "!")

