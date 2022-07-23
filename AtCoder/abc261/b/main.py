n = int(input())
a = [list(input()) for _ in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        t = a[i][j]
        s = a[j][i]

        if (t == 'W' and s == 'L') or (t == 'L' and s == 'W') or (t == 'D' and s == 'D'):
            continue
        else:
            print("incorrect")
            exit()
print("correct")
