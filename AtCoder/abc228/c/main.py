import bisect

N, K = map(int, input().split())
P = [sum(list(map(int, input().split()))) for _ in range(N)]
sorted_P = sorted(P.copy())

for p in P:
    #print(N + 1 - bisect.bisect_right(sorted_P, p + 300))
    if N + 1 - bisect.bisect_right(sorted_P, p + 300) <= K:
        print("Yes")
    else:
        print("No")
