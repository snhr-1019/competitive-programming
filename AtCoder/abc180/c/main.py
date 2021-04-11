N = int(input())

i = 1
ans = []
while i * i <= N:
    if N % i == 0:
        ans.append(i)
        if i * i != N:
            ans.append(N // i)
    i += 1

ans.sort()
for n in ans:
    print(n)
