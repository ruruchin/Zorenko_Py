# Дана непустая строка S и целое число N (> 0). Вывести строку, содержащую символы
# строки S, между которыми вставлено по N символов «*» (звездочка).
word = str(input())
N = int(input("Введите кол-во символов для букав: "))  # Количество повторений символа
symbol = "*"
new_word = ''
for letter in word:
    new_word += letter + (symbol * N)

print(new_word)