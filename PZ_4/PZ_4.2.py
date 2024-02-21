"""
Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма
1 + 2 + ... + K будет меньше или равна N, и саму эту сумму.
"""
N = int(input("Введите целое число N: "))

sum_of_numbers = 0
K = 0

for i in range(1, N+1):
    if K < N and sum_of_numbers <= N:
        K += 1
        sum_of_numbers += i
        if sum_of_numbers > N:
            sum_of_numbers = sum_of_numbers - i
            K -= 1

print(f"Наибольшее K:{K}","Сумма чисел от 1 до K:", sum_of_numbers)

# for i in range(N):
#     if sum_of_numbers < N:
#         K += 1
#         if K < N:
#             sum_of_numbers +=i-1
#
# print(f"Наибольшее K:{K}","Сумма чисел от 1 до K:", sum_of_numbers)



