n = int(input())
s = input()

f = s.find('ABC')
if f == -1:
    print(-1)
else:
    print(f + 1)
