import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    T2 = int(input())

    matrix = []
    matrix2 = []
    count = 0
    for _ in range(1, T2+1):
        # A, B 부터 C, D까지 E(1 빨간색, 2 파란색))
        A, B, C, D, E = map(int, input().split())
        if E == 1:
            for i in range(A, C+1):
                for j in range(B, D+1):
                    # if [i, j] not in matrix:
                    matrix.append([i, j])
        else:
            for i in range(A, C+1):
                for j in range(B, D+1):
                    # if [i, j] not in matrix2:
                    matrix2.append([i, j])
    for i in range(len(matrix2)):
        if matrix2[i] in matrix:
            count += 1
    print(f'#{tc} {count}')