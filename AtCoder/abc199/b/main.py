N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

print(max(0, min(Bs) - max(As) + 1))
