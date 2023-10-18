import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []

    for i in range(N):
        my_list = []
        for j in input():
            my_list += j
        matrix.append(my_list)

    answer = []

    # 수평에서 찾기
    for i in range(N):
        for j in range(N - M + 1):
            A = []
            B = []
            for k in range(M):
                A.append(matrix[i][j+k])
            for k in reversed(range(M)):
                B.append(matrix[i][j+k])
            if A == B:
                answer = A

    # 수직에서 찾기
    for i in range(N - M + 1):
        for j in range(N):
            A = []
            B = []
            for k in range(M):
                A.append(matrix[i+k][j])
            for k in reversed(range(M)):
                B.append(matrix[i+k][j])
            if A == B:
                answer = A

    answer_2 = ''
    for i in answer:
        answer_2 += i

    print(f'#{tc} {answer_2}')