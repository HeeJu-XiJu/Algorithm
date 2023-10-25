def solution(sides):
    my_list = sorted(sides)
    answer = 2
    if max(sides) < my_list[0] + my_list[1]:
        answer = 1
    return answer

print(solution([1, 2, 3]))