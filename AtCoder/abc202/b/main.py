S = input()
mapping = {
    "0": "0",
    "1": "1",
    "6": "9",
    "8": "8",
    "9": "6",
}
ans = ""
for s in S[::-1]:
    ans += mapping[s]
print(ans)
