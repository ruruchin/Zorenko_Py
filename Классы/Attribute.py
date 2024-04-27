class Comment:
    count = 0

    def __init__(self, text):
        self.text = text


    def uppcount(self):
        self.up += 1
        
my_com = Comment
print(my_com.count)
my_com.count = 17
print(my_com.count)
print(Comment.count)