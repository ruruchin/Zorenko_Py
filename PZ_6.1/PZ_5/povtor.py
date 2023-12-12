def row_sum(lsd):

    SUMDIGGER = 0

    for i in range(len(lsd)):
        SUMDIGGER = SUMDIGGER + lsd[i]

    print(f"СУММА ЧИСЛОВОГО РЯДА СПИСКА: {SUMDIGGER}")


N = int(input("ВВЕДИТЕ СКОЛЬКО ЧИСЕЛ ВЫ ХОТИТЕ ДОБАВИТЬ В СПИСОК: "))

lsd = [int(input(f"Введите число {i + 1}: ")) for i in range(N)]
row_sum(lsd)

