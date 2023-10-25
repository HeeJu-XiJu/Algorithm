def solution(numbers):
    answer = []
    for number in numbers:
        N = number * 2
        answer.append(N)
    return answer

print(solution([1, 2, 100, -99, 1, 2, 3]))
