"""Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год
выпуска". От этого класса унаследуйте класс "Автомобиль" и добавьте в него
свойство "тип кузова". """
class Trankquil:
    def mark(self, mark):
        self.mark = mark
        print(f"Марка автотранспорта: {mark}")

    def model(self, model):
        self.model = model
        print(f"Модель автотранспорта {model}")

    def NewYear(self, year=1999):
        self.year = year
        print(f"Год выпуска {year}")


class Authomobile(Trankquil):
    def kuZOV(self, kuzov):
        self.kuzov = kuzov
        print(f"Тип кузова: {kuzov}")

info = Authomobile()
info.kuZOV("Я кузов")
info.NewYear()

