
def funccc(lsd):

    maximum = [lsd[::1]]
    for i in range(len(lsd)-1):
        curent = lsd[i]+lsd[i+1]
        if curent > maximum:
            mix = curent
            print(mix)

N = (int(input("ВВЕДИТЕ РАЗМЕР СПИСКА")))
lsd = [int(input("Введите число для списка: ")) for _ in range(N)]