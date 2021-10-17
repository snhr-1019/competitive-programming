S = input()
arr = [S]
for i in range(len(S)):
    S = S[1:] + S[0]
    arr.append(S)
arr.sort()
print(arr[0])
print(arr[-1])
