N = int(input())

ans = 0
for i in range(1, N+1):
    octval = oct(i)
    if '7' not in str(i) and '7' not in str(octval):
        ans += 1
print(ans)
