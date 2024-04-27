#1. В матрице найти сумму и произведение элементов столбца N (N
#задать с клавиатуры).
#2. В матрице найти отрицательные элементы, сформировать из них новый массив.
#Вывести размер полученного массива.
import random
stroki = int(input("количество строк: "))
colonki = int(input("количество столбцов: "))

matrix = [[random.randint(-2, 10) for _ in range(colonki)] for _ in range(stroki)]

for row in matrix:
    print(row)

N = int(input("Введите номер столбца N: "))
sum_colonki = sum(row[N-1] for row in matrix)
product_column = 1
for row in matrix:
    product_column *= row[N-1]

print("Сумма элементов в столбце N: ", sum_colonki)
print("Произведение элементов в столбце N: ", product_column)

negative_elements = [element for row in matrix for element in row if element < 0]
print("Размер массива с отрицательными элементами: ", len(negative_elements))