from itertools import permutations

S = [input() for _ in range(3)]
chars = set(''.join(S))

if len(chars) > 10:
    print("UNSOLVABLE")
    exit()

chars = list(chars)

idx = {c: i for i, c in enumerate(chars)}

for perm in permutations(range(10)):
    num = []

    # 3種類の文字列のループ
    for s in S:
        n = 0
        # 各文字列について、最初の文字が0の場合は不適
        if perm[idx[s[0]]] == 0:
            break

        # 各文字列の1文字ずつ見て、足してく
        for c in s:
            n = 10 * n + perm[idx[c]]
        num.append(n)

    if len(num) == 3 and num[0] + num[1] == num[2]:
        print(*num, sep="\n")
        exit()

print("UNSOLVABLE")
