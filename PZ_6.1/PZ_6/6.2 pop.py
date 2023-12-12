import random
lsd = []
i = 0
for _ in range(10):
    lsd.append(random.randint(1,10))
lsd.sort()

first = lsd[0]
second = lsd[1]

print(first + second)
