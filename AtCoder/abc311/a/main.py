n = int(input())
s = input()
st = set()
for i in range(n):
    st.add(s[i])
    if len(st) == 3:
        print(i + 1)
        exit()
