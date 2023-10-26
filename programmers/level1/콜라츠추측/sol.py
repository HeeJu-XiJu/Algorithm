def solution(num):
    answer = 0
    i = num
    while i != 1:
        if i % 2 == 0:
            i /= 2
        else:
            i = i * 3 + 1
        answer += 1
        if answer == 500:
            answer = -1
            break

    return answer