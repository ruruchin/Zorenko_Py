"""
Скорость первого автомобиля Vi км/ч, второго - V2
км/ч, расстояние между ними S км. Определить расстояние между ними через Т часов, если автомобили первоначально движутся
навитречу друг другу. Данное расстояние равно модулю разности начального расстояния и общего пути, проделанного
автомобилями;
общий путь - время • суммарная скорость. """



v1 = int(input("введите число км/ч"))
v2 = int(input("введите число км/ч"))
S = int(input("введите кол-во км"))
T = int(input("введите кол-во ч"))
if v1 > 0:
    pass
else:
    print('проверьте правильность написания чисел'), exit()
if v2 > 0:
    pass
else:
    print('проверьте правильность написания чисел'), exit()

if S > 0:
    pass
else:
    print('проверьте правильность написания чисел'), exit()

if T > 0:
    pass
else:
    print('проверьте правильность написания чисел'), exit()

print((v1+v2)*T-S, ' км')