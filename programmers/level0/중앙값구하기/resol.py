def solution(array):
    sort_list = sorted(array)
    a = len(sort_list) // 2
    answer = sort_list[a]

    return answer

print(solution([1, 2, 7, 10, 11]))