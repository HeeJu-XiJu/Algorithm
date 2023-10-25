def solution(numlist, n):
    answer = []
    my_list = []
    numlist2 = numlist
    for i in numlist:
        my_list.append(abs(i - n))

    my_list = sorted(my_list)

    for i in range(len(numlist)):
        if (n + my_list[i]) in numlist2:
            answer.append(n + my_list[i])
            numlist2.remove(n + my_list[i])
        elif (n - my_list[i]) in numlist2:
            answer.append(n - my_list[i])

    return answer

print(solution([1, 2, 3, 4, 5, 6], 4))