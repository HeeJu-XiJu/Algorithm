import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    answer = 0
    T = int(input())
    my_list = list(map(int, input().split()))
    for i in range(2, T-2):
        answer_list = []
        for j in range(i-2, i+3):
            answer_list.append(my_list[j])
        if max(answer_list) == my_list[i]:
            sort_list = sorted(answer_list)
            answer += sort_list[-1] - sort_list[-2]
    print(f'#{tc} {answer}')