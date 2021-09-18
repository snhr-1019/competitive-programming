X = {c: chr(65 + i) for i, c in enumerate(list(input()))}
N = int(input())
S = [input() for _ in range(N)]
S.sort(key=lambda s: "".join([X[c] for c in list(s)]))
print("\n".join(S))
