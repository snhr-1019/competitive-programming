from itertools import permutations

S, K = input().split()
S = list(S)
K = int(K)
S.sort()

st = set()
for i, v in enumerate(permutations(S, len(S))):
    st.add(''.join(v))

st = list(st)
st.sort()

for i, s in enumerate(st):
    if i + 1 == K:
        print(s)
