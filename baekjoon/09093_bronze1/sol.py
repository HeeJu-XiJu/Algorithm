import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

for _ in range(n):
    answer = ''
    words = sys.stdin.readline().split()
    for word in words:
        if answer != '':
            answer += ' '
        stack = []
        for alp in word:
            stack.append(alp)
        while len(stack) != 0:
            answer += stack.pop()

    print(answer)