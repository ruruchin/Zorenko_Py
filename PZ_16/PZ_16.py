"""Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
выводит информацию о животном в формате "Имя: имя, Вид: вид"."""
"""Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате."""
import pickle
class Enimals:
    def __init__(self, name="Имя", vid="Вид", surname=" "):
        self.name = name
        self.surname = surname
        self.vid = vid
        print(f'Имя: {name}')
        print(f"Вид: {vid}")
Info = [
    Enimals("pop", "собак", "god"),
    Enimals("pon", "собак_молодой", "godamn"),
    Enimals("pin", "Коля", "Martin")
]
def save_def(info):
    for i in range(len(info)):
        with open(f"Info_file{i}.bin", 'wb') as file:
            pickle.dump(info[i], file)
def load_def(info):
    for i in range(len(info)):
        with open(f"Info_file{i}.bin", 'rb') as file:
            info = pickle.load(file)
            print(info.__dict__)

save_def(Info)
load_def(Info)
"""
.dump -> ввод
.load -> выгрузка(чтение)
    /|
   /|||                   
  ||||||                       
 ||||||||                 
||||||||||                               
    ||                      
    ||
    ||                             
=========================   
"""
info = Enimals()
info.__init__("pop", "собак", "god")