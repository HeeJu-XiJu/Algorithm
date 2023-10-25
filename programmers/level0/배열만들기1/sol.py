def solution(n, k):
    answer = []
    for i in range(1, n+1):
        if i % k == 0:
            answer.append(i)
    return answer

print(solution(10, 3))

# 다른 풀이
def solution(n, k):
    return [i for i in range(k, n+1, k)]