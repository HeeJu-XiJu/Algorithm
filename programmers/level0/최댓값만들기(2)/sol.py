def solution(numbers):
    answer = -10000000000
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] * numbers[j] > answer:
                answer = numbers[i] * numbers[j]
    return answer

print(solution([1, 2, -3, 4, -5]))