def solution(A, B):
    rev = ''
    number = 0
    while number != len(A):
        if rev == B:
            answer = 1
        rev = A[-1] + A[0:len(A)-2]
        number += 1

    answer = 0
    return answer