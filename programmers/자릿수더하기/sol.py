def solution(n):
    answer = 0
    for number in str(n):
        answer += int(number)
    return answer

print(solution(930211))


