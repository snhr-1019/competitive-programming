y = int(input())

a = y % 4


if a == 2:
    print(y)
elif a == 0:
    print(y + 2)
elif a == 1:
    print(y + 1)
elif a == 3:
    print(y + 3)
