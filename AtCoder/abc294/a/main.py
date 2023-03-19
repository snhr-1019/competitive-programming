n = int(input())
a = list(map(int, input().split()))
for ai in a:
    if ai % 2 == 0:
        print(ai)
