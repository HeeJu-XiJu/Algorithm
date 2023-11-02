# Question

def solution(n, lost, reserve):
    # any = []
    reserve = sorted(reserve)
    # reserve.sort()
    for i in reserve:
        if i in lost:
            # any.append(i)
            lost.remove(i)
        else:
            if i-1 in lost and i not in lost:
                lost.remove(i-1)
            elif i+1 in lost and i not in lost:
                lost.remove(i+1)
            
    answer = n - len(lost)
    return answer

print(solution(5, [4, 5], [4, 3]))