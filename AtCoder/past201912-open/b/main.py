n = int(input())
a = [int(input()) for _ in range(n)]

for i in range(n - 1):
    if a[i + 1] == a[i]:
        print("stay")
    elif a[i + 1] < a[i]:
        print("down " + str(a[i] - a[i + 1]))
    else:
        print("up " + str(a[i + 1] - a[i]))
