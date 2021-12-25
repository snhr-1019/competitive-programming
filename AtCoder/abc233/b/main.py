L, R = map(int, input().split())
S = input()
L -= 1
print(S[0:L] + ''.join(reversed(S[L:R])) + S[R:])