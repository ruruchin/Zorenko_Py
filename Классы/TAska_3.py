class Commet:
    def __init__(self, text):
        self.text = text


    @staticmethod
    def merge_comment(first, second):
        return f"{first} {second}"

info = Commet("my_commet")
info_1 = Commet.merge_comment("Судоку,","Глина")
print(info_1)
