n = int(input())
mn = 10 ** 10
mn_i = -1
S = []
for i in range(n):
    s, a = input().split()
    a = int(a)
    S.append(s)
    if a < mn:
        mn = a
        mn_i = i

for j in range(n):
    print(S[(mn_i + j) % n])

