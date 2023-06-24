n = int(input())
s = input()

ans = []
start = -1

stack = [[]]
for i in range(n):
    if s[i] == '(':
        stack.append(['('])
    elif len(stack) > 1 and s[i] == ')':
        stack.pop()
    else:
        stack[-1].append(s[i])

for st in stack:
    print(*st, sep='', end='')

