def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        for i in num_list:
            answer *= i
    return answer

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))