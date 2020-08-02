k = int(input())

i = -1
num = 0
while True:
    if k % 2 == 0:
        print(-1)
        exit(0)
    i += 1
    num += (7*10**i)
    num %= k

    if num % k == 0:
        print(i+1)
        exit(0)

