n, q = map(int, input().split())
s = list(input())

head = 0
for _ in range(q):
    t, x = input().split()
    x = int(x)
    if t == '1':
        head -= x
        head %= n
    else:
        print(s[(head + x - 1) % n])
