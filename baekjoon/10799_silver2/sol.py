import sys
sys.stdin = open('input.txt')

a = input()

stack = []
answer = 0
for n in range(len(a)) :
    if a[n] == '(':
        stack.append('(')
    else:
        if a[n-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
        
print(answer)