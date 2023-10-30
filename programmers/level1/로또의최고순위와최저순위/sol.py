def solution(lottos, win_nums):
    answer = []
    count = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            count += 1
        elif i == 0:
            zero += 1

    min = 0
    max = 0

    if count != 0 :
        min = 7-count
    else:
        min = 6
    
    if min <= zero:
        max = 1
    else:
        max = min - zero

    answer.append(max)
    answer.append(min)

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))