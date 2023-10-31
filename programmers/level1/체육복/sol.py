# Question

def solution(n, lost, reserve):
    # any = []
    reserve = sorted(reserve)
    # reserve.sort
    for i in reserve:
        if i-1 in lost and i not in lost:
            lost.remove(i-1)
        elif i+1 in lost and i not in lost:
            lost.remove(i+1)
        
        if i in lost:
            # any.append(i)
            lost.remove(i)
            
    answer = n - len(lost)
    return answer

print(solution(5, [1, 2, 3, 4, 5], [1, 2, 4, 5]))