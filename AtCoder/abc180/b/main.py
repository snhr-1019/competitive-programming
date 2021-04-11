N = int(input())
X = list(map(int, input().split()))

md = 0
ud = 0
cd = 0
for x in X:
    md += abs(x)
    ud += pow(x, 2)
    cd = max(cd, abs(x))

print(md)
print(pow(ud, 0.5))
print(cd)
