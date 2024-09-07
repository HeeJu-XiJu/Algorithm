def solution(n):
    answer = 0
    for i in range(1, n+1):
        a = n
        while a != 0:
            a -= i
            if a == 0:
                answer += 1
                break
            elif a < 0:
                break
            i += 1
    return answer

print(solution(15))