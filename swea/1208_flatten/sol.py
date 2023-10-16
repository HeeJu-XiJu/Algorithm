import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    my_list = list(map(int, input().split()))
    for tc2 in range(T):
        my_list = sorted(my_list)
        my_list[-1] = my_list[-1] - 1
        my_list[0] = my_list[0] + 1
        if my_list[-1] - my_list[0] < 1:
            break
    answer = max(my_list) - min(my_list)
    print(f'#{tc} {answer}')