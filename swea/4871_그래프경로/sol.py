import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    matrix = []
    for i in range(V+1):
        matrix.append([0] * (V+1))

    for i in range(E):
        A, B = map(int,input().split())
        matrix[A][B] = 1
    
    C, D = map(int, input().split())

    # 방문 체크리스트
    check_list = [False] * (V + 1)

    # DFS용 stack
    stack = []

    # v부터 시작
    v = C
    check_list[v] = True
    stack.append(v)

    while len(stack):
        for w in range(V+1):
            # 연결된 것을 확인
            if matrix[v][w] == 1:
                # 아직 방문하지 않았다면
                if check_list[w] == False:
                    #  나의 위치를 stack에 push
                    stack.append(v)
                    check_list[w] = True

                    # w를 현재 위치로 변경
                    v = w

                    if w == D:
                        answer = 1

                    break
        # break를 만나지 않은 경우
        # 방문하지 않은 정점이 없는 경우
        # 과거의 위치로 돌아가기
        else:
            v = stack.pop()

    print(answer)
