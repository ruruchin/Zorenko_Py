def maxi_sum(listic):
    if len(listic) < 2:
        return "Список слишком мал"

    max_sum = listic[0] + listic[1]
    max_index = 0

    for i in range(1, len(listic) - 1):
        current_sum = listic[i] + listic[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_index = i
    final = [listic[max_index], listic[max_index + 1]]

    final.sort()

    final.reverse()

    return final

N = int(input("Введите размер списка: "))
listic = [int(input(f"Введите элемент списка под номером {i+1}: ")) for i in range(N)]
result = maxi_sum(listic)
print(f"Два соседних элемента с максимальной суммой: {result}")
