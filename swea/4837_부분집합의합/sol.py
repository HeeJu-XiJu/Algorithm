import sys
sys.stdin = open('input.txt')

T = int(input())
my_list = range(1, 13)

for tc in range(1, T+1):
    N, M = map(int, input().split())

    answer = 0
    for i in range(1<<12):
        temp = []
        for j in range(12):
            if i & (1 << j):
                temp.append(my_list[j])
        if len(temp) == N and sum(temp) == M:
            answer += 1
    print(f'#{tc} {answer}')