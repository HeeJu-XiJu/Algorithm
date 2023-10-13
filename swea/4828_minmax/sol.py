import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))
    for i in range(0, len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]

    print(f'#{tc} {my_list[-1] - my_list[0]}')