N, K = map(int, input().split())


def f(n):
    N = len(str(n))
    ret = 0
    arr = sorted(list(map(int, str(n))), reverse=True)
    for i in range(len(arr)):
        ret += (arr[i] - arr[N - i - 1]) * 10 ** (N - i - 1)
    return ret


for i in range(K):
    N = f(N)
print(N)
