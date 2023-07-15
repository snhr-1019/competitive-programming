n = int(input())

st = set()
for _ in range(n):
    s1 = input()
    s2 = s1[::-1]
    st.add(min(s1, s2))
print(len(st))
