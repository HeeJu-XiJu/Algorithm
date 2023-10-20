def solution(num, total):
    num_total = 0
    for i in range(num):
        num_total += i
    n = int((total - num_total) / num)

    answer = []
    for i in range(n, n+num):
        answer.append(i)

    return answer

print(solution(5, 15))