# Дана строка-предложение на русском языке. Вывести самое короткое слово в
# предложении. Словом считать набор символов, не содержащий пробелов, знаков препинания и
# ограниченный пробелами, знаками препинания или началом/концом строки.
import re

print(min(str(re.sub(r"[.,!123456789]", '', input("Введите ваше предложение: "))).split()))
# predlo = str(re.sub(r"[.,]", ' ', input("Введите ваше предложение: "))).split()
#
# small_word = predlo[0]
#
# for letter in predlo:
#     if len(letter) <= len(small_word):
#         small_word = letter
# print(small_word)







