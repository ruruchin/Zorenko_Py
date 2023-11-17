def SortDec3(A,B,C):
 '''Сортировка для (N) чисел по убыванию'''
N = int(input("Введите сколько чисел вы хотите отсортировать и внести в список: "))
my_SortList = [int(input()) for _ in range(N)]
print('-' * 20)
print("ДО СОРТИРОВКИ: ", my_SortList)
my_SortList.sort(reverse=True)

print("ПОСЛЕ СОРТИРОВКИ: ", my_SortList)
print('-' * 20)