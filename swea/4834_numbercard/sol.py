import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    numbers = str(input())
    
    my_list = [0] * 10

    # number 갯수 list 만들기
    for i in numbers:
        my_list[int(i)] += 1

    # 최댓값 출력
    a = 0
    for j in range(9, 0, -1):
        if my_list[j] > a:
            a = my_list[j]
            b = j

    print(f'#{tc} {b} {a}')
