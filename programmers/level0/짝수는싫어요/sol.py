def solution(n):
    my_list = []
    for numbers in range(1, n + 1):
        if numbers % 2 != 0:
            my_list.append(numbers)
    answer = my_list
    return answer

print(solution(10))