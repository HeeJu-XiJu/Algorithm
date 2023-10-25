def solution(n):
    answer = 0
    for N in range(1, n+1):
        if N % 2 == 0:
            answer += N
    return answer

# def solution(n):
#     numbers = range(2, n+1, 2)
#     return sum(numbers)


print(solution(10))
print(solution(4))