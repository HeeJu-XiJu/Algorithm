def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer

print(solution([1, 8, 3]))