def solution(A, B):
    rev = A
    number = 0
    answer = -1
    while number != len(A):
        if rev == B:
            answer = number
            break
        rev = rev[-1] + rev[0:len(A)-1]
        number += 1
    return answer

print(solution('apple', 'elppa'))