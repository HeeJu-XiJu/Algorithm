def solution(num_list):
    e = 0
    o = 0
    answer = []
    for num in num_list:
        if num % 2 == 0:
            e += 1
        else:
            o += 1
    answer.append(e)
    answer.append(o)
    return answer

print(solution([1, 3, 5, 7]))