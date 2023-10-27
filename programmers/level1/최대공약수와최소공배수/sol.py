import math

def solution(n, m):
    lcm = 0
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            lcm = i
            break
    answer = [math.gcd(n, m), lcm]
    return answer
    
print(solution(3, 12))