"""Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
выводит информацию о животном в формате "Имя: имя, Вид: вид"."""

class Enimals:
    def Name_vid(self, name="Имя", vid="Имя"):
        self.name = name
        self.vid = vid
        print(f'Имя: {name}')
        print(f"Вид: {vid}")

info = Enimals()
info.Name_vid("Прикол","прекол")







