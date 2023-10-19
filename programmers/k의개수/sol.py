def solution(i, j, k):
    my_list = []
    for i in range(i, j+1):
        my_list += (str(i))
    
    answer = my_list.count(str(k))

    return answer


print(solution(1, 13, 1))