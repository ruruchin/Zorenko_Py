word = str(input())
N = int(input("Введите кол-во символов для букав: "))  # Количество повторений символа
symbol = "*"

new_word = ''
for letter in word:
    new_word += letter + (symbol * N)

print(new_word)




