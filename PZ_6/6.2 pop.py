# Дан список размера N. Найти два соседних элемента, сумма которых максимальна, и вывести эти элементы в порядке возрастания их индексов.


import random
lsd = []
i = 0
for _ in range(10):
    lsd.append(random.randint(1,10))
lsd.sort()

first = lsd[0]
second = lsd[1]
print(second,'\n',first)
print(first + second)
