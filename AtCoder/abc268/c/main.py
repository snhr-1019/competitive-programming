n = int(input())
p = list(map(int, input().split()))

cnt = [0] * n

# 料理iに着目
for i in range(n):
    # 人i-jに移動させるために必要な操作回数を求めて、cntに+1する
    for j in range(-1, 2):
        cnt[(i - j - p[i]) % n] += 1

print(max(cnt))
