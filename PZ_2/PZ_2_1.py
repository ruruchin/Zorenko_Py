#Дано двузначное число. Найти сумму и произведение его цифр.
#try:
chislo=int(input("Введите двузначное число: "))
if chislo > 0:
    chislo_1 = chislo % 10
    chislo_2 = chislo // 10
    slochenie = chislo_1 + chislo_2
    proizvedenie = chislo_1 * chislo_2
else:
    print("Введите положительное число")
#except TypeError:
 #   print("Вы ввели не число")
print("Результат суммы цифр числа:",slochenie)
print("Результат произведения цифр числа:",proizvedenie)