def solution(triangle):
    for yidx in range(len(triangle)):
        for xidx in range(len(triangle[yidx])):
            if yidx == 0:
                continue
            elif xidx == 0 or yidx == 1:
                triangle[yidx][xidx] += triangle[yidx-1][0]
            elif xidx == len(triangle[yidx])-1:
                triangle[yidx][xidx] += triangle[yidx-1][xidx-1]
            else:
                triangle[yidx][xidx] += max(triangle[yidx-1][xidx], triangle[yidx-1][xidx-1])
    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


# 다른 풀이
def solution(triangle):

    height = len(triangle)

    while height > 1:
        for i in range(height - 1):
            triangle[height-2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer