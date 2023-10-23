# Вариант 12.
# 1. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Каждое из
# чисел A, B, C положительное».



print("Ваша задача ввести (!)ПОЛОЖИТЕЛЬНЫЕ(!) => (!)ЦЕЛЫЕ(!) числа")
from function import glitch
from function import postglitch



glitch()
postglitch()
print("Перезапустить программу?"'\n'"ДА/НЕТ")
perezapyck = str(input())
if perezapyck == "ДА":
    print("Ваша задача ввести (!)ПОЛОЖИТЕЛЬНЫЕ(!) => (!)ЦЕЛЫЕ(!) числа")

    a = input("Введите ваше первое число ^-^: ")
    b = input("Введите ваше второе число ^-^: ")
    c = input("Введите ваше третье число ^-")
    glitch()
    postglitch()
elif perezapyck =="НЕТ":
    print("Конец программы"),exit()
else:
    exit()


