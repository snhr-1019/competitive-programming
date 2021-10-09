N, M = map(int, input().split())
A = [list(input()) for _ in range(2 * N)]
ranking = [[i, 0] for i in range(2 * N)]


def janken(s, t):
    if s == t:
        return 0
    elif s == "G" and t == "C" or s == "C" and t == "P" or s == "P" and t == "G":
        return 1
    else:
        return -1


# iラウンド
for i in range(M):
    # k位とk+1位が勝負
    for k in range(N):
        a = ranking[2 * k][0]
        b = ranking[2 * k + 1][0]
        result = janken(A[a][i], A[b][i])
        if result == 1:
            ranking[2 * k][1] += 1
        elif result == -1:
            ranking[2 * k + 1][1] += 1
    ranking.sort(key=lambda x: (-1 * x[1], x[0]))
    # print(ranking)

print(*map(lambda x: x[0] + 1, ranking), sep='\n')
