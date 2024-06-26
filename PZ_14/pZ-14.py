import re
'''
•1	Найдите все натуральные числа (возможно, окружённые буквами);
•2	Найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв);
•3	Найдите слова, в которых есть русская буква, а за ней цифра;
•4	Найдите все слова, начинающиеся с русской или латинской большой буквы (\b — граница слова);
•5	Найдите слова, которые начинаются на гласную (\b — граница слова);
•6	Найдите все натуральные числа, не находящиеся на границе слова;
•7	Найдите строчки, в которых есть символ * (. — это точно не конец строки!);
•8	Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки;
•9	Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами);
•10	Выделите одним махом только текстовую часть оглавления, без тегов;
•11 Найдите пустые строчки;
•12	Найти все теги, не включая их содержимое.
'''
'''------------------------------'''
'''
1) Ответ: \d+ 
2) Ответ: [А-Я]
3) Ответ: [А-Яа-я]+[\d]
4) Ответ: \w+[A-ZА-Я]+\w+
5) Ответ: - \b[AEIOUYАИОЯЮЁУЕЫЭ]\w+
6) Ответ: - \B[0-9]\B
7) Ответ: - 
8) Ответ: - [()]+
9) Ответ: - (<.*>)
10) Ответ: -
11) Ответ: -(\n)
12) Ответ: -
'''
'''------------------------------'''
p = re.compile(r"[0-9]+$",re.S)
if p.search("32543151"):
    print("Число")
else:
    print("НЕ ЧИСЛО!!")
'''---------------------------------------------------'''
slovo = re.compile(r"\bГандон\b")
print("Найдено" if slovo.search("Гандон ебаный")else "Не найдено")
print("Найдено" if slovo.search("Гандон") else "Ну нормально")
'''---------------------------------------------------'''
ili = re.compile(r"красн((ая)|(ый)|(ое))")
print("НАЙДЕНО" if ili.search("красное")else "БОООО")
'''---------------------------------------------------'''
s = "<b>123sdgsg</b><b>123gsdsdg</b>123lsdjg124;<b>ak124sjvk</b>"
soot = re.compile(r"<b>(.*?)</b>")
print(soot.findall(s))
'''---------------------------------------------------'''
search = re.compile(r"[0-9]+")
print("Нормис" if search.match("str123") else "Нет")
print("yfdsfj" if search.match("str123", 3) else "bobo")
#search.match("str123", 3) <- 3, это хуйня про счет с 3 пункта, а не по всей строке
'''---------------------------------------------------'''
pythin = re.compile("[Pp]ython")
print("Найдено" if pythin.fullmatch("Python") else "Нет")
'''----------------------------------------------------'''
goda = re.compile(r"[0-9]+")
print(goda.findall("20015,15,151636,361,3661,2,412,516,163"))
'''----------------------------------------------------'''
goida = re.compile(r"[0-9]+")
print(goida.subn("Гойда","20015,15,151636,361,3661,2,412,516,163"))
'''----------------------------------------------------'''
stroka = "Гойда братья и сёстры, задеваеШЬ?"
print(re.sub("Гойда","Своим примером",stroka))
'''----------------------------------------------------'''





