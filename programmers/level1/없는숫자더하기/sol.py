def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

# 다른 풀이
answer = sum(range(10)) - sum(numbers)