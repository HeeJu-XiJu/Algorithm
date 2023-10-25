def solution(order):
    str_order = str(order)
    answer = 0
    for i in str_order:
        if int(i) % 3 == 0 and int(i) != 0:
            answer += 1
    return answer

print(solution(29423))