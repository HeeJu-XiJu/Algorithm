def solution(num_list):
    answer = []
    for number in range(1, len(num_list) + 1):
        answer.append(num_list[-(number)])
    return answer

print(solution([1, 0, 1, 1, 1, 3, 5]))