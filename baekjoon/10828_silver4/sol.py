import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
stack = []

for idx in range(1, n+1):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        stack.append(int(com[1]))
    elif com[0] == 'top':
        if len(stack) != 0:
            a = stack.pop()
            stack.append(a)
            print(a)    
        else:
            print(-1)
    elif com[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
            