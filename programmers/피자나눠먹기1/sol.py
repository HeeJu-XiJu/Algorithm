def solution(n):
    answer = 0
    while (7 * answer) // n < 1:
        answer += 1
    return answer

print(solution(15))