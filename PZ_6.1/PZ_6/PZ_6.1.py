N = int(input())
if N % 2 !=0:
    MY_LIST = [x for x in range(N) if x % 2 !=0]
    MY_LIST = MY_LIST[::2]
    MY_LIST.reverse()
    print(*MY_LIST)
else:
    print("FALSE")