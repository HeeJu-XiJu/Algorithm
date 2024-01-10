def solution(n, computers):
    def DFS(n, num1, computers):
            for num2 in range(n):
                if computers[num1][num2] == 1:
                    computers[num1][num1] = 0
                    computers[num1][num2] = 0
                    computers[num2][num1] = 0
                    computers[num2][num2] = 0
                    DFS(n, num2, computers)

    answer = 0
    for num1 in range(n):
        if 1 in computers[num1]:
            answer += 1
            DFS(n, num1, computers)
    
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))