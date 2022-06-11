r, c = map(int, input().split())
r -= 1
c -= 1

a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))

print(a[r][c])
