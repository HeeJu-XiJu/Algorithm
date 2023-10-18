def solution(array):
    A = array
    A.sort()
    if len(A) % 2 == 0:
        answer = (A[len(A) // 2] + A[((len(A) // 2) - 1)] / 2)
    else:
        answer = A[((len(A) + 1) // 2) - 1]
    return answer

print(solution([1, 2, 7, 10, 11]))
