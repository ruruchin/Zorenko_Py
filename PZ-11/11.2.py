# Открываем файл и выводим его содержимое на экран
with open('text18-12.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# пробелы
space_count = content.count(' ')


with open('poem_text.txt', 'w', encoding='utf-8') as new_file:
    lines = content.split('\n')
    for line in lines:
        new_file.write(line + '\n' + '*'*len(line) + '\n')

# Выводим количество пробельных символов
print(f'Количество пробельных символов: {space_count}')