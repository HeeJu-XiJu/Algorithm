import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    answer = []

    for char in input():
        if answer and char == answer[-1]:
            answer.pop()
        else :
            answer.append(char)
    
    print(f'#{tc} {len(answer)}')