
# Дан список A размера N (N — нечетное число). Вывести его элементы с нечетными номерами в порядке убывания номеров: AN, AN-2, AN-4, ..., A1. Условный оператор не использовать
import random
list = []
for _ in range(12):
    list.append(random.randint(0,11))
print(list)
K = int(input("Введите число сдвигов и первых элементов положенных нулю: "))
if K < 2:
    print("Введите K больше 1!",'\n',"FALSE")
else:
    for _ in range(K):
        list.insert(0, 0)
    print(list)























