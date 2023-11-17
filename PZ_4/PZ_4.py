"""
* Дано целое число N (>0). Найти значение выражения 1.1 - 1.2 + 1.3 - ... (N слагаемых,
* знаки чередуются). Условный оператор не использовать.
"""
def calculate_expression(N):
    result = 0.0
    digit = 1.0

    for i in range(1, N + 1):
        result += digit * (1.0 + i / 10)
        digit = -digit  # меняем знак

    return result


N = int(input("Введите целое число N (>0): "))
result = calculate_expression(N)
print(f"Значение выражения для N = {N}: {result}")