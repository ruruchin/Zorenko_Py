# Из списка: ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия'] получить новый список, в котором длина слов не превышает 5 символов.
lst_name=['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
new = [name for name in lst_name if len(name) <=5]
print(new)