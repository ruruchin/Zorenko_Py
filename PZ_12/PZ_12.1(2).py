from random import randint
tripletick = [randint(-2, 2) for xxx in range(10) if xxx>0]
new=[xx for xx in tripletick if xx>0]
print(tripletick)
print(new)

print(f'Положительные числа {len(new)}')




