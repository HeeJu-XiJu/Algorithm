import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
answer = deque()

for _ in range(n):
    com = sys.stdin.readline().split()

    if com[0] == 'push_front':
        answer.appendleft(com[1])
    elif com[0] == 'push_back':
        answer.append(com[1])
    elif com[0] == 'pop_front':
        if len(answer) != 0:
            print(answer.popleft())
        else:
            print(-1)
    elif com[0] == 'pop_back':
        if len(answer) != 0:
            print(answer.pop())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(answer))
    elif com[0] == 'empty':
        if len(answer) != 0:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if len(answer) != 0:
            a = answer.popleft()
            print(a)
            answer.appendleft(a)
        else:
            print(-1)
    elif com[0] == 'back':
        if len(answer) != 0:
            a = answer.pop()
            print(a)
            answer.append(a)
        else:
            print(-1)