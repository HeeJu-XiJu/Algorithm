# def solution(A,B):
#     answer = 0
#     for i in range(1, len(A)+1):
#         answer += sorted(A)[i-1] * sorted(B)[-i]
#     return answer


# def solution(A,B):
#     mlist = []
#     for i in range(1, len(A)+1):
#         mlist.append(sorted(A)[i-1] * sorted(B)[-i])
#     answer = sum(mlist)
#     return answer

def solution(A,B):
    A = sorted(A) 
    B = sorted(B)[::-1]
    answer= sum(A[i] * B[i] for i in range(len(A)))
    return answer

print(solution([1, 4, 2], [5, 4, 4]))