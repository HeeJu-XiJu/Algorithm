import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 숫자갯수
    # M : 합할 숫자 갯수
    N, M = map(int, input().split())
    my_list = list(map(int, input().split()))
    answer_list = []
    for i in range(N-M+1):
        answer = 0
        for j in range(M):
            answer += my_list[i+j]
        answer_list.append(answer)
    my_max = max(answer_list)
    my_min = min(answer_list)

    answer = my_max - my_min

    print(f'#{tc} {answer}')