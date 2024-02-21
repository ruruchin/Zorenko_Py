# Дан список размера N. Найти два соседних элемента, сумма которых максимальна, и вывести эти элементы в порядке возрастания их индексов.
import random

# lsd = []
# for _ in range(10):
# lsd.append(random.randint(1, 10))
lsd =[random.randint(1,10) for _ in range(10)]
lsd.sort(reverse=True)
print(lsd)

first = lsd[0]
second = lsd[1]

print(first, '+', second, '=', f'{second+first}', sep=' ')

print(second+first)
