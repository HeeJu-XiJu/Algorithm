import sys
sys.stdin = open('input.txt')

T = int(input())

def search(idx):
    global SUM, MIN_SUM

    if idx >= N:
        if SUM < MIN_SUM:
            MIN_SUM = SUM
        return

    # 모든 경우의 수를 탐색    
    for i in range(N):
        # 해당칸이 비어있다면
        if check_list[i] == False:
            # result.append(matrix[idx][i])
            SUM += matrix[idx][i]
            check_list[i] = True
            search(idx+1)
            # result.pop()
            SUM -= matrix[idx][i]
            check_list[i] = False

for tc in range(1, T+1):
    N = int(input())

    matrix = []
    for i in range(N):
        matrix.append(list(map(int,input().split())))

    result = []
    check_list = [False] * N

    SUM = 0
    MIN_SUM = 100000000

    search(0)

    print(f'#{tc} {MIN_SUM}')