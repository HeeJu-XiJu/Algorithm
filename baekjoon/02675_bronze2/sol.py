import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(1, T+1):
    a, b = map(str, input().split())
    answer = ''
    for char in b:
        answer += char * int(a)
    print(answer)