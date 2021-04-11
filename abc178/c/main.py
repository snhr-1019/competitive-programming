N = int(input())
mod = 1000000007
if N == 1:
    print(0)
else:
    a = 10 ** N % mod
    b = 9 ** N % mod
    c = 8 ** N % mod
    print((a - 2 * b + c) % mod)
