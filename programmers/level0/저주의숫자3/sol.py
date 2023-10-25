def solution(n):
    answer = 1
    real = 1

    while n != real:
        real += 1
        answer += 1

        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
            
    return answer

print(solution(40))