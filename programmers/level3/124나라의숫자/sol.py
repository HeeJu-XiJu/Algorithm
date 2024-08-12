def solution(n):
    answer = ''
    while n:
        t = n % 3
        if not t:
            answer += '4'
            n -= 1
        else:
            answer += str(t)
        n //= 3
    return answer[::-1]

print(solution(10))