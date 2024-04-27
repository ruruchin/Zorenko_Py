class Note:#NoteTask = тайл текст натация
    def __init__(self, text):
        self.text = text
        self.count = 0

    def upcount(self, digit):
        self.count += digit

    def ResetCount(self):
        self.count = 0

note1 = Note
print(note1.upcount(10))
print(note1.__dict__)

