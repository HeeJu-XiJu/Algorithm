def solution(numbers):
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer

print(solution([0, 31, 24, 10, 1, 9]))