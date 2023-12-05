# Вариант 12.
# 2. Дано целое число. Вывести его строку-описание вида «отрицательное четное
# число», «нулевое число», «положительное нечетное число» и т. д.
print("Введите ЧИСЛО: ")
znachenie = ''
number = int(input())
if number == 0:
    print("нулевое число"),exit()

if number <0:
    znachenie += "отрицательное  "
else:
    znachenie += "положительное "

if number % 2 == 0:
    znachenie += "четное число"
else:
    znachenie += "нечетное число"
print(number,"=>",znachenie)

znachenie = 3 if number ==0 else znachenie = 4






