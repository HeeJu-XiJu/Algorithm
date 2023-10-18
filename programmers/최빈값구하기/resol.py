def solution(array):
    count = 0
    answer = 0
    same = 0

    for i in array:
        if array.count(i) > count :
            count = array.count(i)
            answer = i
            same = 0
        elif array.count(i) == count and i != answer :
            same += 1

    if same >= 1:
        answer = -1

    return answer

print(solution([1, 1, 2, 2]))