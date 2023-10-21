def solution(a, b):
    import math

    GCD = math.gcd(a, b)
    rev_b = b // GCD
    my_list = []

    while rev_b != 1:
        for i in range(2, int(rev_b) + 1):
            while rev_b % i == 0:
                my_list.append(i)
                rev_b /= i
    
    while 2 in my_list :
        my_list.remove(2)

    while 5 in my_list :
        my_list.remove(5)

    if len(my_list) == 0:
        answer = 1
    else:
        answer = 2

    return answer

print(solution(7, 40))