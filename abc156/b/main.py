n, k = map(int, input().split())
nbase = ''
tmp = n
while tmp > 0:
    nbase += str(tmp % k)
    tmp = int(tmp / k)

print(len(nbase))
