
from random import randrange, random, randint
tripletick = [randint(-100, 100) for xxx in range(100) if xxx > 0]
new=[xx for xx in tripletick if xx>0]
for plus in new:
    if plus >0:
        plus +=1
print(new)
print(tripletick)
print(f'НУ НОРМАЛЬНЫЕ ЧИСЛА -> {plus}')




