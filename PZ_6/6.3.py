# # Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
# # списка вправо на K позиций (при этом A1 перейдет в AK+1, A2 — в AK+2, ..AN-K — в
# # AN, а исходное значение K последних элементов будет потеряно). Первые K
# # элементов полученного списка положить равными 0.

import random
# Lsd = [int(input(f"Введите {x+1} число: "))for x in range(10)]
# K = int(input("Введите сдвиг: "))
# for i in range(K):
#     Lsd.insert(0, 0)
# print(Lsd)
# for _ in range(100):
#     list.append(random.randint(0,100))
list = [random.randint(1,10) for i in range(10)]
print(list)
K = int(input("Введите число сдвигов и первых элементов положенных нулю: "))
if K < 2:
    print("Введите K больше 1!",'\n',"FALSE")
else:
    for _ in range(K):
        list.insert(0, 0)
    print(list)





