class Image:
    def Resolution(self):
        self.resolution = 720
        #self.resize = print(input("Задайте новый размер картинки:"))
    def Resize(self):
        self.resize = print(input("Задайте новый размер картинки:"))

    def Title(self, text_title):
        self.title = text_title

    def Extension(self, extension):
        self.extension = extension

    def title_upper(self, upper_text):
        self.upper_text = print(input("Введите текст: "))


info = Image()
print(info.Resize())