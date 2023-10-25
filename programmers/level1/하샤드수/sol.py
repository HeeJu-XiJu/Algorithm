def solution(x):
    answer = False
    total = 0
    for i in str(x):
        total += int(i)

    if x % total == 0:
        answer = True

    return answer

print(solution(11))