from collections import deque
S = input()
l = len(S)

stack = deque()
box = set()
for s in S:
    if s == '(':
        stack.append(set())
    elif s == ')':
        T = stack.pop()
        for t in T:
            box.discard(t)
    else:
        if s in box:
            print("No")
            exit()
        else:
            box.add(s)
            if stack:
                stack[-1].add(s)
print("Yes")
