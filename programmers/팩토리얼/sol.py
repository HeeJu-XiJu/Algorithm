def solution(n):
    count = 1
    answer = 1
    while count <= n:
        answer += 1
        count *= answer
    return answer-1

print(solution(3628800))
print(solution(7))