def solution(n):
    answer = 1
    f_n1 = 0
    f_n2 = 1

    count = 2

    while count != n:
        f_n1 = f_n2
        f_n2 = answer
        answer = f_n1 + f_n2
        count += 1

    return answer % 1234567

print(solution(5))