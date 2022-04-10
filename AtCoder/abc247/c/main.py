def s(n):
    if memo[n] != "":
        return memo[n]
    if n == 1:
        ret = "1"
    else:
        ret = s(n - 1) + " " + str(n) + " " + s(n - 1)
    memo[n] = ret
    return ret


n = int(input())
memo = [""] * (n + 1)
print(s(n))
