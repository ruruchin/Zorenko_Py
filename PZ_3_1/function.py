a = input("Введите ваше первое число ^-^: ")
b = input("Введите ваше второе число ^-^: ")
c = input("Введите ваше третье число ^-^: ")

def glitch():
    global a,b,c
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            print("!","Введите правильный тип данных","!",sep=' ')
            a = input("Введите ваше число a: ")
    while type(b) != int:
        try:
            b = int(b)
        except ValueError:
            print("!", "Введите целоe положительное число", "!", sep=' ')
            b = input("Введите ваше число b: ")

    while type(c) != int:
        try:
            c = int(c)
        except ValueError:
            print("!", "Введите целоe положительное число", "!", sep=' ')
            c = input("Введите ваше число c: ")
def postglitch():
    if a > 0 and b > 0 and c > 0:
        print("ВАШИ ВВЕДЕННЫЕ ЧИСЛА ПОЛОЖИТЕЛЬНЫ!!!!!!!!!!!!!")
    else:
        print("!","ВВЕДИТЕ ЧИСЛА СОГЛАСНО УСЛОВИЮ","!",sep=' ')


