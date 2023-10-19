def solution(dots):
    sort = sorted(dots)
    length = abs(sort[0][0] - sort[2][0])
    height = abs(sort[0][1] - sort[1][1])
    answer = length * height
    return answer

print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))