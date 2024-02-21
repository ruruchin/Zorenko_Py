# Дан список A размера N (N — нечетное число). Вывести его элементы с нечетными
# номерами в порядке убывания номеров: AN, AN-2, AN-4, ..., A1. Условный оператор не
# использовать.

import random
Diapazon = int(input("число должно быть нечетным: "))
if Diapazon % 2 != 0:
    # My_list = [random.randint(1, 10) for _ in range(10)]
    My_list = [x for x in range(Diapazon + 1) if x % 2 != 0]
    My_list = My_list[::1]
    My_list.reverse()
    print(My_list)

else:
    print("False")




