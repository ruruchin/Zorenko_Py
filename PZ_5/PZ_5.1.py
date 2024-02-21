# Составить функцию, которая выполнит суммирования числового ряда
N = int(input("Сколько чисел вы хотите суммировать?: "))
def SlistDigit():

    SDigit = 0

    My_row_list = [int(input()) for _ in range(N)]

    for digit in My_row_list:
        SDigit += digit
    print(SDigit)

SlistDigit()









