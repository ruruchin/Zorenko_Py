import pickle
class User:
    def __init__(self,name:str,pol:str,age:int):
        self.name = name
        self.pol = pol
        self.age = age
Info=[
    User("pop", "Мужской", 124),
    User("pon", "Женский", 14),
    User("pin", "Женский", 1)
]
def save_load(info):
    for i in range(len(info)):
        with open(f"Info_file{i}.bin", 'wb')as file:
            pickle.dump(info[i], file)
    for i in range(len(info)):
        with open(f"Info_file{i}.bin",'rb')as file:
            info = pickle.load(file)
            print(info.__dict__)

save_load(Info)








