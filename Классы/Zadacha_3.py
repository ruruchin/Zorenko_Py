class Person:
    count = 0
    def __init__(self,name):
        self.name = name
    @staticmethod
    def up(count):
        return count

info = Person("Джон сноу")
print(info.up(10))
print(Person.count)
