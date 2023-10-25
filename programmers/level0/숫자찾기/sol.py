def solution(num, k):
    answer = -1
    str_num = str(num)
    for i in range(len(str_num)):
        if int(str_num[i]) == k:
            answer = i + 1
            break
    return answer

print(solution(29183, 1))