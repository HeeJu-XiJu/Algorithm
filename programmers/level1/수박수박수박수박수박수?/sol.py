def solution(n):
    answer = ''
    num = 0
    while num != n:
        if num % 2 == 0:
            answer += '수'
        else:
            answer += '박'
        num += 1
    return answer