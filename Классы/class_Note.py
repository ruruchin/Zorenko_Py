class Note:
    def __init__(self, text):
        self.text = text
        self.count = 0

    def upcount(self):
        self.count += 1


note1 = Note("Задача 1")
note2 = Note("Задача 2")
print(note1.__dict__)#формирует словарь из атрибутов которые пришли в класс(переменную класса)

#print(note2.__dict__)

#print(dir(note1))#Вывод всевозможных параметров
print(note1.text)

note1.upcount()
print(
note1.count
)
print(note1.upcount)
print(Note.upcount)
#print(note1.count)

#note1.reset_count()
#print(note1.count)