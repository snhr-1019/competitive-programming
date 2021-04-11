r1, c1 = list(map(int, input().split()))
r2, c2 = list(map(int, input().split()))

dr = abs(r2-r1)
dc = abs(c2-c1)

if r1 == r2 and c1 == c2:
    print(0)
elif r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2) + abs(c1-c2) <= 3:
    print(1)
elif abs(c2 - (c1+dr)) <= 3 or abs(c2 - (c1-dr)) <= 3 or abs(r2 - (r1+dc)) <= 3 or abs(r2 - (r1-dc)) <= 3:
    print(2)
elif (r1+c1) % 2 == (r2+c2) % 2:
    print(2)
else:
    print(3)
