k, x = map(int, input().split())
l = max(x-k+1, -1000000)
r = min(x+k-1,  1000000)
for i in range(l, r+1):
    print(i)
