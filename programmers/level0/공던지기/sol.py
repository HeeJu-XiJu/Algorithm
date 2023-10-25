def solution(numbers, k):
    a = 2 * (k-1)
    length = len(numbers)
    order = a % length
    answer = numbers[order]
    return answer

print(solution([1, 2, 3], 3))