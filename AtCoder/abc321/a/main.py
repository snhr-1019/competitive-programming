n = input()
l = len(n)

if l == 1:
    print("Yes")
else:
    for i in range(1, l):
        if int(n[i]) >= int(n[i - 1]):
            print("No")
            exit()
    print("Yes")
