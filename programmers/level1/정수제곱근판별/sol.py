def solution(n):
    answer = -1
    if (n ** 0.5) % 1 == 0:
        answer = ((n ** 0.5) + 1) ** 2
    return answer

print(solution(121))