N = int(input())
S = []
T = []
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)

for i in range(N):
    for j in range(i + 1, N):
        if T[i] == T[j] and S[i] == S[j]:
            print("Yes")
            exit()
print("No")
