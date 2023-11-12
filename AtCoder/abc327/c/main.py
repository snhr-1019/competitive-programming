a = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    if len(set(a[i])) != 9:
        print("No")
        exit()

    if len(set([a[j][i] for j in range(9)])) != 9:
        print("No")
        exit()

for i in range(3):
    for j in range(3):
        if len(set([a[i * 3 + k][j * 3 + l] for k in range(3) for l in range(3)])) != 9:
            print("No")
            exit()
print("Yes")
