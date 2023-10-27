def solution(price, money, count):
    own = 0
    for i in range(1, count+1):
        own += price * i
    answer = own - money
    if answer < 0:
        answer = 0
    return answer

# 다른 풀이
range(1, n+1)의 합 = (n+1) * n // 2