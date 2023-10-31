def solution(n, lost, reserve):
    reserve.sort()
    for j in reserve:
        if j in lost:
            lost.remove(j)
            reserve.remove(j)

    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
            

    answer = n - len(lost)
    return answer