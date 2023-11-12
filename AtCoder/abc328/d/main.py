from collections import deque

s = input()
stack = deque()

for si in s:
    stack.append(si)
    if len(stack) >= 3 and (stack[-3], stack[-2], stack[-1]) == ('A', 'B', 'C'):
        stack.pop()
        stack.pop()
        stack.pop()

print(''.join(stack))
