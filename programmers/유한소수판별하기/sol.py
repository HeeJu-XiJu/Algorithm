def solution(a, b):
    import math

    GCD = math.gcd(a, b)
    rev_b = b / GCD

    if rev_b % 2 != 0 or rev_b % 5 != 0:
        answer = 2
    else :
        answer = 1
    return answer

print(solution(12, 21))