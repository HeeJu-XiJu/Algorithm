import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

def VP(input):
    stack = []
    for str in input:
        if str == '(':
            stack.append(str)
        elif str == ')' and len(stack) != 0:
            stack.pop()
        elif str == ')' and len(stack) == 0:
            return print('NO')
    if len(stack):
        return print('NO')
    else:
        return print('YES')


for _ in range(n):
    VP(sys.stdin.readline())