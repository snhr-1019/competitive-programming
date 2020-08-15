x, k, d = map(int, input().split())

if abs(x) // d > k:
    print(abs(x) - k * d)
else:
    tmp = abs(x) - d * (abs(x) // d)
    if (k - abs(x) // d) % 2 == 0:
        print(tmp)
    else:
        print(abs(tmp - d))
