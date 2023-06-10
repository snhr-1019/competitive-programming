n = int(input())
t1 = n // 5 * 5
t2 = t1 + 5
if n - t1 < t2 - n:
    print(t1)
else:
    print(t2)
