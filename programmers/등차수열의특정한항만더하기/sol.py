def solution(a, d, included):
    answer = 0
    idx = 0
    for TF in included:    
        if TF:
            answer += (a + (d * idx))
            idx += 1
        else:
            idx += 1
    return answer

print(solution(3, 4, [True, False, False, True, True]))