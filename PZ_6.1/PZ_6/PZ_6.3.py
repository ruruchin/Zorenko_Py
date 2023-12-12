import random
# Lsd = [int(input(f"Введите {x+1} число: "))for x in range(10)]
# K = int(input("Введите сдвиг: "))
# for i in range(K):
#     Lsd.insert(0, 0)
# print(Lsd)
list = []
for _ in range(100):
    list.append(random.randint(0,100))
print(list)
K = int(input("Введите число сдвигов и первых элементов положенных нулю: "))
if K < 2:
    print("Введите K больше 1!",'\n',"FALSE")
else:
    for _ in range(K):
        list.insert(0, 0)
    print(list)