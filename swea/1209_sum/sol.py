import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 100 X 100 2차원으로 만들기
    T = input()
    my_list = []

    for i in range(100):
        numbers = list(map(int, input().split()))
        my_list.append(numbers)

    answer_sum = 0

    # 수평 합 구하기
    for i in range(100):
        if answer_sum < sum(my_list[i][0:100]):
            answer_sum = sum(my_list[i][0:100])

    # 수직 합 구하기
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += my_list[j][i]
        if answer_sum < col_sum:
            answer_sum = col_sum

    # 대각선 합 구하기(좌상 -> 우하)
    diagonal_sum = 0
    for i in range(100):
        diagonal_sum += my_list[i][i]
    if answer_sum < diagonal_sum:
        answer_sum = diagonal_sum

    # 대각선 합 구하기(우상 -> 좌하)
    diagonal2_sum = 0
    for i in range(100):
        diagonal2_sum += my_list[i][99-i]
    if answer_sum < diagonal2_sum:
        answer_sum = diagonal2_sum
        
    print(f'#{T} {answer_sum}')
