"""
Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма
1 + 2 + ... + K будет меньше или равна N, и саму эту сумму.
"""
N = int(input("Введите целое число N: "))

sum_of_numbers = 0
K = 0

for i in range(N+1):
    if sum_of_numbers <= N:
        sum_of_numbers += i
        K += 1
    else:
        break

print(f"Наибольшее K:{K}","Сумма чисел от 1 до K:", sum_of_numbers)
