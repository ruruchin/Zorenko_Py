#Дано двузначное число. Найти сумму и произведение его цифр.
chislo=int(input("Введите двузначное число: "))
chislo_1 = chislo % 10
chislo_2 = chislo // 10
slochenie = chislo_1 + chislo_2
proizvedenie = chislo_1 * chislo_2
print("Результат суммы цифр числа:",slochenie, sep=' ')
print("Результат произведен цифр числа:",proizvedenie, sep=' ')