n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
m = max(a)
for ai in a:
    if ai != m:
        print(ai)
        exit()
