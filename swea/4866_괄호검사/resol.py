import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    stack = []

    for char in input():
        if char == '{' or char == '(':
            stack.append(char)
        elif len(stack) != 0 and char == ')' and stack[-1] == '(':
            stack.pop()
        elif len(stack) != 0 and char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)

    if len(stack) > 0:
        answer = 0
    else:
        answer = 1

    print(f'#{tc} {answer}')
