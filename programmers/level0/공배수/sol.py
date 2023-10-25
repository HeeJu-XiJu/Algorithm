def solution(number, n, m):
    answer = int(not(number % n) and not(number % m))
    return answer