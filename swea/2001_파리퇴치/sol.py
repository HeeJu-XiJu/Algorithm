import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    my_list = []
    N, M = map(int, input().split())
    for i in range(N):
        my_list2 = list(map(int, input().split()))
        my_list.append(my_list2)

    answer = 0
    
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total = 0
            for k in range(M):
                for l in range(M):
                    total += my_list[i+k][j+l]
                    
            if total > answer:
                answer = total
            
    print(f'#{tc} {answer}')




