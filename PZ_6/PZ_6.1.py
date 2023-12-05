Diapazon = int(input("число должно быть нечетным: "))
if Diapazon % 2 !=0:
    My_list = [x for x in range(Diapazon +1) if x %2 !=0 ]
    My_list = My_list[::2]
    My_list.reverse()
    print(My_list)
else:
    print("False")




