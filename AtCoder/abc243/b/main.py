n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Bs = set(B)

hit = 0
blow = 0

for i in range(n):
    if A[i] == B[i]:
        hit += 1
    elif A[i] in Bs:
        blow += 1

print(hit)
print(blow)
