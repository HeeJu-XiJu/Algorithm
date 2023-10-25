def solution(sides):
    sort_side = sorted(sides)
    A, B = sort_side
    # B가 가장 클 때
    # B < A + N
    # 미지수가 가장 클 때
    # N < A + B

    answer = 2 * A - 1

    return answer


print(solution([11, 7]))